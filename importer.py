import pandas as pd 
from sqlalchemy import create_engine
engine = create_engine('postgresql://arnikausername:arnikapassword@localhost:5432/finance_v2_db')

df_company=pd.read_csv('company.csv')
df_company=df_company[df_company['source']=='rahsar']
df_company['national_id'] = df_company['national_id'].astype(str) + 'i'
df_company.to_csv('company_cl.csv',index=False)
df_company=pd.read_csv('company_cl.csv')
df_company=df_company[['name','national_id','source','is_active','group_id','industry_id','is_confirmed']]
breakpoint()
df_company.to_sql('company_info', engine, index=False, if_exists='append')
# df_company_info=pd.read_sql('select * from company_info',engine)
# print(df_company.columns)
breakpoint()
df_company_list=df_company['id'].unique()
df_financial_statement=pd.read_csv('financial_statement.csv')
df_financial_statement=df_financial_statement[df_financial_statement['company_id'].isin(df_company_list)]
df_financial_statement.to_csv('financial_statement_cl.csv')
df_financial_statement=pd.read_csv('financial_statement_cl.csv')
df_financial_statement_list=df_financial_statement['id'].unique()
df_financial_statement_detail=pd.read_csv('financial_statement_detail.csv')
df_financial_statement_detail=df_financial_statement_detail[df_financial_statement_detail['statement_id'].isin(df_financial_statement_list)]
df_financial_statement_detail.to_csv('financial_statement_detail_cl.csv')
# df_financial_statement=df_financial_statement[df_financial_statement['source']=='rahsar']
# df_company.merge(df_financial_statement,how='right',on='')