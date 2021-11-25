import streamlit as st
import pandas as pd
import numpy as np
import base64



st.set_page_config(layout="wide")
st.title('Simulationstool')


st.write('Wertungsmatrix')
col1, col2, col3, col4, col5 =st.beta_columns(5)


with col1:

    proc_bieter_1= st.number_input('% für Bieter 1', value = 100)
    proc_bieter_1 = proc_bieter_1/100


    faktor_block_1_anb1= st.number_input('Faktor Block 1 Grundausstattung für Bieter 1', value  = 100)
    faktor_block_1_anb1 = faktor_block_1_anb1/100

    faktor_block_2_anb1= st.number_input('Faktor Block 2 Grundkörper für Bieter 1', value  = 100)
    faktor_block_2_anb1 = faktor_block_2_anb1/100

    faktor_block_3_anb1= st.number_input('Faktor Block 3 Dienstleistung für Bieter 1', value = 100)
    faktor_block_3_anb1 = faktor_block_3_anb1/100

    faktor_block_4_anb1= st.number_input('Faktor Block 4 Bauleistungen für Bieter 1', value = 100)
    faktor_block_4_anb1 = faktor_block_4_anb1/100

    faktor_block_5_anb1= st.number_input('Faktor Block 5 Ersatzteile für Bieter 1', value = 100)
    faktor_block_5_anb1 = faktor_block_5_anb1/100



with col2:
    proc_bieter_2= st.number_input('% für Bieter 2', value =  80)
    proc_bieter_2 = proc_bieter_2/100

    faktor_block_1_anb2= st.number_input('Faktor Block 1 Grundausstattung für Bieter 2', value  = 100)
    faktor_block_1_anb2 = faktor_block_1_anb2/100

    faktor_block_2_anb2= st.number_input('Faktor Block 2 Grundkörper für Bieter 2', value  = 100)
    faktor_block_2_anb2 = faktor_block_2_anb2/100

    faktor_block_3_anb2= st.number_input('Faktor Block 3 Dienstleistung für Bieter 2', value = 100)
    faktor_block_3_anb2 = faktor_block_3_anb2/100

    faktor_block_4_anb2= st.number_input('Faktor Block 4 Bauleistungen für Bieter 2', value = 100)
    faktor_block_4_anb2 = faktor_block_4_anb2/100

    faktor_block_5_anb2= st.number_input('Faktor Block 5 Ersatzteile für Bieter 2', value = 100)
    faktor_block_5_anb2 = faktor_block_5_anb2/100



with col3:
    proc_bieter_3= st.number_input('% für Bieter 3', value =  60)
    proc_bieter_3 = proc_bieter_3/100

    faktor_block_1_anb3= st.number_input('Faktor Block 1 Grundausstattung für Bieter 3', value  = 100)
    faktor_block_1_anb3 = faktor_block_1_anb3/100

    faktor_block_2_anb3= st.number_input('Faktor Block 2 Grundkörper für Bieter 3', value  = 100)
    faktor_block_2_anb3 = faktor_block_2_anb3/100

    faktor_block_3_anb3= st.number_input('Faktor Block 3 Dienstleistung für Bieter 3', value = 100)
    faktor_block_3_anb3 = faktor_block_3_anb3/100

    faktor_block_4_anb3= st.number_input('Faktor Block 4 Bauleistungen für Bieter 3', value = 100)
    faktor_block_4_anb3 = faktor_block_4_anb3/100

    faktor_block_5_anb3= st.number_input('Faktor Block 5 Ersatzteile für Bieter 3', value = 100)
    faktor_block_5_anb3 = faktor_block_5_anb3/100



with col4:
    proc_bieter_4= st.number_input('% für Bieter 4', value =  120)
    proc_bieter_4 = proc_bieter_4/100

    faktor_block_1_anb4= st.number_input('Faktor Block 1 Grundausstattung für Bieter 4', value  = 100)
    faktor_block_1_anb4 = faktor_block_1_anb4/100

    faktor_block_2_anb4= st.number_input('Faktor Block 2 Grundkörper für Bieter 4', value  = 100)
    faktor_block_2_anb4 = faktor_block_2_anb4/100

    faktor_block_3_anb4= st.number_input('Faktor Block 3 Dienstleistung für Bieter 4', value = 100)
    faktor_block_3_anb4 = faktor_block_3_anb4/100

    faktor_block_4_anb4= st.number_input('Faktor Block 4 Bauleistungen für Bieter 4', value = 100)
    faktor_block_4_anb4 = faktor_block_4_anb4/100

    faktor_block_5_anb4= st.number_input('Faktor Block 5 Ersatzteile für Bieter 4', value = 100)
    faktor_block_5_anb4 = faktor_block_5_anb4/100






with col5:
    proc_bieter_5= st.number_input('% für Bieter 5', value = 100)
    proc_bieter_5 = proc_bieter_5/100

    faktor_block_1_anb5= st.number_input('Faktor Block 1 Grundausstattung für Bieter 5', value  = 100)
    faktor_block_1_anb5 = faktor_block_1_anb5/100

    faktor_block_2_anb5= st.number_input('Faktor Block 2 Grundkörper für Bieter 5', value  = 100)
    faktor_block_2_anb5 = faktor_block_2_anb5/100

    faktor_block_3_anb5= st.number_input('Faktor Block 3 Dienstleistung für Bieter 5', value = 100)
    faktor_block_3_anb5 = faktor_block_3_anb5/100

    faktor_block_4_anb5= st.number_input('Faktor Block 4 Bauleistungen für Bieter 5', value = 100)
    faktor_block_4_anb5 = faktor_block_4_anb5/100

    faktor_block_5_anb5= st.number_input('Faktor Block 5 Ersatzteile für Bieter 5', value = 100)
    faktor_block_5_anb5 = faktor_block_5_anb5/100







df_preis = pd.read_excel('df_preis.xlsx')
df_preis = df_preis.drop('Unnamed: 0', axis=1)
data = pd.read_excel('wertungsmatrix_blocks.xlsx',  sheet_name=None, header=0)

df_sum = pd.DataFrame()


for bieter in range(1,6):
    if bieter == 1:
        faktor_block_1 = faktor_block_1_anb1
        faktor_block_2 = faktor_block_2_anb1
        faktor_block_3 = faktor_block_3_anb1
        faktor_block_4 = faktor_block_4_anb1
        faktor_block_5 = faktor_block_5_anb1
        proc_bieter = proc_bieter_1
    elif bieter == 2:
        faktor_block_1 = faktor_block_1_anb2
        faktor_block_2 = faktor_block_2_anb2
        faktor_block_3 = faktor_block_3_anb2
        faktor_block_4 = faktor_block_4_anb2
        faktor_block_5 = faktor_block_5_anb2
        proc_bieter = proc_bieter_2
    elif bieter == 3:
        faktor_block_1 = faktor_block_1_anb3
        faktor_block_2 = faktor_block_2_anb3
        faktor_block_3 = faktor_block_3_anb3
        faktor_block_4 = faktor_block_4_anb3
        faktor_block_5 = faktor_block_5_anb3
        proc_bieter = proc_bieter_3
    elif bieter == 4:
        faktor_block_1 = faktor_block_1_anb4
        faktor_block_2 = faktor_block_2_anb4
        faktor_block_3 = faktor_block_3_anb4
        faktor_block_4 = faktor_block_4_anb4
        faktor_block_5 = faktor_block_5_anb4
        proc_bieter = proc_bieter_4
    elif bieter == 5:
        faktor_block_1 = faktor_block_1_anb5
        faktor_block_2 = faktor_block_2_anb5
        faktor_block_3 = faktor_block_3_anb5
        faktor_block_4 = faktor_block_4_anb5
        faktor_block_5 = faktor_block_5_anb5
        proc_bieter = proc_bieter_5
    for i in list(data.keys()):
        df_sum_temp = pd.DataFrame()
        if i in ['Block 1', 'Block 2', 'Block 3', 'Block 4', 'Block 5']:


            w_matr = pd.read_excel('wertungsmatrix_blocks.xlsx', sheet_name =i, header=0)
            #w_matr['OZ'] = w_matr['OZ'].astype(str)
            #w_matr['OZ'] = w_matr['OZ'].str.replace('.', '')
            w_matr['OZ'] = w_matr['OZ'].astype(float)
            block_1 = w_matr
            #block_1 = pd.merge(w_matr, df_preis, how='left', on = 'OZ')

            block_1['Einheitspreis'] = block_1['Einheitspreis'] * proc_bieter
            if i == 'Block 1':
                block_1['Faktor Block'] = faktor_block_1
            elif i == 'Block 2':
                block_1['Faktor Block'] = faktor_block_2
            elif i == 'Block 3':
                block_1['Faktor Block'] = faktor_block_3
            elif i == 'Block 4':
                block_1['Faktor Block'] = faktor_block_4
            elif i == 'Block 5':
                block_1['Faktor Block'] = faktor_block_5
            block_1['Faktor x Preis'] = block_1['Einheitspreis'] * block_1['Wichtungs-\nFaktor'] * block_1['Faktor Block']
            block_1['Einheitspreis']=block_1['Einheitspreis'].fillna(0)
            block_1['Faktor x Preis']= block_1['Faktor x Preis'].fillna(0)


            df_sum_temp = df_sum_temp.append(block_1[['Einheitspreis', 'Faktor x Preis']].sum(), ignore_index=True)
            df_sum_temp['% vom Einheitspreis'] =proc_bieter *100
            df_sum_temp['Faktor Block'] = block_1['Faktor Block'][0]
            df_sum_temp['Bieter'] =bieter
            df_sum_temp['Block'] =i
            df_sum = pd.concat([df_sum, df_sum_temp])

resul = pd.pivot_table(df_sum, values=['Einheitspreis', 'Faktor x Preis'], index=['Bieter', 'Block', 'Faktor Block', '% vom Einheitspreis'],   aggfunc='sum', fill_value=None, margins=False, dropna=True)
resul.reset_index(inplace=True)
resul = resul.sort_values('Bieter', axis=0, ascending=True)
resul = resul.rename(columns={'Einheitspreis': 'Preis'})
resul_sum = resul.groupby('Bieter')[['Preis', 'Faktor x Preis']].sum().round(2)
resul_sum.reset_index(inplace=True)
resul_sum= resul_sum.sort_values('Faktor x Preis', axis=0, ascending=True)
st.title('Wertungsmatrix Summary')
st.table(resul_sum)

st.title('Details')
st.table(resul)

#writer = pd.ExcelWriter('wertungsmatrix_blocks.xlsx', engine='xlsxwriter')
for i in list(data.keys()):
    if i in ['Block 1', 'Block 2', 'Block 3', 'Block 4', 'Block 5']:
        w_matr = pd.read_excel('wertungsmatrix_blocks.xlsx', sheet_name =i, header=0)
        w_matr['OZ'] = w_matr['OZ'].astype(float)
        block_ = w_matr
       # block_ = block_.drop('Preis', axis=1)



        # Write each dataframe to a different worksheet.
        #block_.to_excel(writer, sheet_name=i, index=False)





        st.title(i)
        st.table(block_)
# Close the Pandas Excel writer and output the Excel file.
#writer.save()
