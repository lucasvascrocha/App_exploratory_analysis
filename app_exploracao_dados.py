#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import base64
import seaborn as sns
import matplotlib.pyplot as plt




# ------------------------------ IMPORTAÇÃO DA TABELA -------------------------------

def get_table_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href


def main():
    st.image('https://media.giphy.com/media/d1E2HXeuONnx5YfC/giphy.gif', width=200)
    st.title('App para Análise exploratória de dados')
    st.subheader('Inclui funções para corte de linhas e colunas')
    file  = st.file_uploader('Escolha a base de dados que deseja analisar (.csv)', type = 'csv')
    if file is not None:
        st.subheader('Analisando os dados')
        df = pd.read_csv(file)
        st.markdown('**Número de linhas:**')
        st.markdown(df.shape[0])
        st.markdown('**Número de colunas:**')
        st.markdown(df.shape[1])
        st.markdown('**Visualizando o dataframe**')
        number = st.slider('Escolha o numero de linhas que deseja vizualizar', min_value=1, max_value=df.shape[0])
        st.dataframe(df.head(number))
        st.markdown('**Nome das colunas:**')
        st.markdown(list(df.columns))
        
        
# ------------------------------ OPÇÃO DE CORTE E MANIPULAÇÃO DA TABELA -------------------------------


        check = st.checkbox('Caso precise cortar linhas ou colunas do DF original clique aqui')
        if check:
            st.subheader('Seleção da parte da tabela que deseja separar')   
            row_init = int(st.number_input(label='Número da linha onde deseja iniciar o corte - Pressione enter e avançe para o próximo campo'))
            st.markdown(row_init)
            row_end = int(st.number_input(label='Número da linha onde deseja finalizar o corte - Pressione enter e avançe para o próximo campo'))
            st.markdown(row_end)
            df = df[row_init:row_end+1]
            st.dataframe(df)
            check = st.checkbox('Clique aqui para cortar colunas')
            if check:
                col_cut = st.multiselect("Selecione as colunas que deseja cortar", df.columns.tolist())
                st.write(col_cut)
                df.drop(col_cut,axis=1, inplace=True)
                st.dataframe(df)
            st.subheader('Faça download da tabela manipulada abaixo : ')
            st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                
          
       # ------------------------------ INÍCIO DA EXPLORAÇÃO -------------------------------
    
    
        st.markdown('**Resumo dos Dados**')
        select_analise = st.radio('Escolha uma análise abaixo :', ('head', 'info', 'describe', 'faltantes'))
        if select_analise == 'head':
            st.dataframe(df.head())
        if select_analise == 'info':
            st.dataframe({'Dtype': df.dtypes, 'Non-Null Count': df.count()})
        if select_analise == 'describe':
            st.dataframe(df.describe())
        if select_analise == 'faltantes':
            st.dataframe(pd.DataFrame({'nomes' : df.columns, 'tipos' : df.dtypes, 'NA #': df.isna().sum(), 'NA %' : (df.isna().sum() / df.shape[0]) * 100})) 
        
        st.subheader('**Análise Exploratória**')
        sns.set_style('whitegrid')
        plt.tight_layout()
        plt.figure(figsize=(12,8))
        if st.checkbox("Correlação entre colunas"):
            st.markdown('Mapa geral de correlação')
            sns.heatmap(df.corr(),annot=True,cmap='coolwarm')
            st.pyplot()
            col_corr = st.multiselect("Selecione a coluna que deseja correlacionar", df.columns.tolist())
            if col_corr:
                st.markdown('Correlação por coluna')
                st.dataframe(df.corr()[col_corr])
        if st.checkbox("Pair plot"):
            sns.pairplot(df)
            st.pyplot()
        if st.checkbox("Histograma"):
            st.markdown('selecione uma coluna para ver seu histograma')
            option = st.selectbox('Selecione uma coluna',list(df.columns))
            num_bins = st.slider('Escolha o numero de bins', min_value=5, max_value=df.shape[0])
            plt.hist(sorted(df[option]),bins=num_bins)
            st.pyplot()
        if st.checkbox("Bar Plot"):
            st.markdown('Selecione as colunas que deseja plotar')
            col1 = st.selectbox('Variável x',list(df.columns))
            col2 = st.selectbox('Variável y',list(df.columns))
            sns.barplot(df[col1],df[col2])
            st.pyplot()
        if st.checkbox("Scatter Plot"):
            st.markdown('Selecione as colunas que deseja plotar')
            col1 = st.selectbox('Variável x',list(df.columns))
            col2 = st.selectbox('Variável y',list(df.columns))
            plt.scatter(df[col1],df[col2])
            st.pyplot()
        if st.checkbox("Box Plot"):
            st.markdown('Selecione as colunas que deseja plotar')
            col1 = st.selectbox('Variável x',list(df.columns))
            col2 = st.selectbox('Variável y',list(df.columns))
            sns.boxplot(df[col1],df[col2])
            st.pyplot()
        if st.checkbox("Count Plot"):
            st.markdown('Selecione a coluna que deseja plotar')
            col1 = st.selectbox('Variável x',list(df.columns))
            sns.countplot(df[col1])
            st.pyplot()
        if st.checkbox("Swarm Plot"):
            st.markdown('Selecione as colunas que deseja plotar')
            col1 = st.selectbox('Variável x',list(df.columns))
            col2 = st.selectbox('Variável y',list(df.columns))
            sns.swarmplot(df[col1],df[col2])
            st.pyplot()
            
# ------------------------------ FIM DA EXPLORAÇÃO -------------------------------
        st.subheader('Obrigado!')
        st.markdown('Desenvolvido por: Lucas Vasconcelos Rocha')
        st.markdown('email para contato: lucas.vasconcelos3@gmail.com')
        st.markdown('Portfólio: https://github.com/lucasvascrocha')
        
        
        
        
            

            
        
        
            
            
        
       
        
if __name__ == '__main__':
    main()


# In[ ]:




