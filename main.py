import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import json
import os
st.set_page_config(page_title="Self Finance App", page_icon='💸' ,layout="wide")
ctf='categories.json'
if 'categories' not in st.session_state:
    st.session_state.categories={
        'Uncategorized':[],
    }
if os.path.exists(ctf):
    with open(ctf, 'r') as f:
        st.session_state.categories = json.load(f)
def save_categories():
    with open(ctf, 'w') as f:
        json.dump(st.session_state.categories, f)
def categorize(df):
    df['Category']='Uncategorized'
    for category,keywords in st.session_state.categories.items():
        if category=='Uncategorized' or not keywords:
            continue
        lk=[keyword.lower().strip() for keyword in keywords]
        for idx, row in df.iterrows():
            details=row['Details'].lower().strip()
            if details in lk:
                df.at[idx, 'Category'] = category
    return df

def load_transactions(file):
    try:
        df=pd.read_csv(file)
        df.columns=[col.strip() for col in df.columns]
        df['Amount']=df['Amount'].str.replace(',','').astype(float)
        df['Date']=pd.to_datetime(df['Date'],format="%d %b %Y")
        
        return categorize(df)
    except Exception as e:
        st.error(f"Error loading file: str{e}")
        return None
def add_keyword_to_category(category, keyword):
    keyword=keyword.strip()
    if keyword and keyword not in st.session_state.categories[category]:
        st.session_state.categories[category].append(keyword)
        save_categories()
        return True
    return False

def main():
    st.title("Finance Dashboard")
    uploaded_file = st.file_uploader("Upload your Transaction CSV file ", type=["csv"])
    if uploaded_file is not None:
        df= load_transactions(uploaded_file)
        if df is not None:
            debit_df=df[df['Debit/Credit']=='Debit'].copy()
            credit_df=df[df['Debit/Credit']=='Credit'].copy()
            st.session_state.debit_df = debit_df.copy()
            tab1,tab2= st.tabs(["Expenses (Debit)", "Payments (Credit)"])
            with tab1:
                new_cat= st.text_input("Add New Category")
                add_button = st.button("Add Category")
                if add_button and new_cat:
                    if new_cat not in st.session_state.categories:
                        st.session_state.categories[new_cat] = []
                        save_categories()
                        st.rerun()
                st.subheader("Your Expenses")
                edited_df=st.data_editor(
                    st.session_state.debit_df[['Date', 'Details', 'Amount', 'Category']],
                    column_config={
                        'Date': st.column_config.DateColumn('Date',format='DD/MM/YYYY'),
                        'Amount':st.column_config.NumberColumn('Amount',format='%.2f AED'),
                        'Category': st.column_config.SelectboxColumn(
                            'Category',
                            options=list(st.session_state.categories.keys())
                        )
                    },
                    hide_index=True,
                    use_container_width=True,
                    key='Category_editor'
                )
                save_buttons=st.button("Apply Changes", type='primary')
                if save_buttons:
                    for idx, row in edited_df.iterrows():
                        new_category = row['Category']
                        if new_category == st.session_state.debit_df.at[idx, 'Category']:
                            continue
                        details = row['Details']
                        st.session_state.debit_df.at[idx, 'Category'] = new_category
                        add_keyword_to_category(new_category, details)
                st.subheader("Expenses Summary")
                category_totals = st.session_state.debit_df.groupby('Category')['Amount'].sum().reset_index()
                category_totals = category_totals.sort_values('Amount', ascending=False)         
                st.dataframe(
                    category_totals,
                    column_config={
                        'Amount':st.column_config.NumberColumn('Amount',format='%.2f AED'),
                    },
                    hide_index=True,
                    use_container_width=True
                )     
                fig=px.pie(
                    category_totals,
                    values='Amount',
                    names='Category',
                    title='Expenses by Category',
                    # color_discrete_sequence=px.colors.qualitative.Pastel
                )
                st.plotly_chart(fig, use_container_width=True)         
            with tab2:
                st.subheader('Payments Summary')
                total_payments= credit_df['Amount'].sum()
                st.metric("Total Payments", f"{total_payments:,.2f} AED")
                st.write(credit_df)
            

main()