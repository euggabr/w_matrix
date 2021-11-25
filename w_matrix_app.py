import streamlit as st
import pandas as pd
import numpy as np
import base64



st.set_page_config(layout="wide")
st.title('Simulationstool')

df_sum = pd.DataFrame()
df_preis = pd.read_excel('df_preis.xlsx')
df_preis = df_preis.drop('Unnamed: 0', axis=1)

data = pd.read_excel('0.2-Wertungsmatrix 21FEA52724 RV FT EUGEN Bieter VR.xlsm',  sheet_name=None, header=0)
col1, col2, col3 =st.beta_columns(3)
with col1:

    proc_bieter_1= st.number_input('% für Bieter 1', value = 100)
    proc_bieter_1 = proc_bieter_1/100

    proc_bieter_4= st.number_input('% für Bieter 4', value =  120)
    proc_bieter_4 = proc_bieter_4/100
    df_sum_temp = pd.DataFrame()

    faktor_block_1= st.number_input('Faktor Block 1 Grundausstattung', value  = 100)
    faktor_block_1 = faktor_block_1/100


    faktor_block_4= st.number_input('Faktor Block 4 Bauleistungen', value = 100)
    faktor_block_4 = faktor_block_4/100



    counter = 0
    for i in list(data.keys())[1:]:
        if i in ['Block 1', 'Block 2', 'Block 3', 'Block 4', 'Block 5']:
            print(i)
            counter = counter+1
            w_matr = pd.read_excel('0.2-Wertungsmatrix 21FEA52724 RV FT EUGEN Bieter VR.xlsm', sheet_name =i, header=0)

            w_matr['OZ'] = w_matr['OZ'].astype(str)


            w_matr['OZ'] = w_matr['OZ'].str.replace('.', '')



            w_matr['OZ'] = w_matr['OZ'].astype(float)

            block_1 = pd.merge(w_matr, df_preis, how='left', on = 'OZ')
            block_1['Einheitspreis'] = block_1['Einheitspreis'] * proc_bieter_1
            block_1['Faktor Block']= 1
            block_1['Faktor x Preis'] = block_1['Einheitspreis'] * block_1['Wichtungs-\nFaktor'] * block_1['Faktor Block']
            #block_1['Faktor x Preis'] = block_1['Einheitspreis'] * block_1['Wichtungs-\nFaktor']
            block_1['Einheitspreis']=block_1['Einheitspreis'].fillna(0)
            block_1['Faktor x Preis']= block_1['Faktor x Preis'].fillna(0)
            block_1.append(block_1[['Einheitspreis', 'Faktor x Preis']].sum(), ignore_index=True)
            #block_1['Preis'] = block_1['Einheitspreis']
            #block_1 = block_1.drop('Einheitspreis', axis=1)



            df_sum_temp = df_sum_temp.append(block_1[['Einheitspreis', 'Faktor x Preis']].sum(), ignore_index=True)
            #df_sum_temp['Faktor'] = block_1['Faktor x Preis'] / block_1['Einheitspreis']
            #df_sum_temp['Faktor'] = block_1['Wichtungs-\nFaktor']
            df_sum_temp['% vom Einheitspreis'] =proc_bieter_1 *100

            df_sum_temp['Faktor Block'] = block_1['Faktor Block'][0]
            df_sum_temp['Bieter'] =1
            df_sum_temp['Block'] =i
            df_sum = pd.concat([df_sum, df_sum_temp])
    #st.table(df_sum)




#st.table(block_1)
with col2:
    counter =0
    proc_bieter_2= st.number_input('% für Bieter 2', value =  80)
    proc_bieter_2 = proc_bieter_2/100

    proc_bieter_5= st.number_input('% für Bieter 5', value = 100)
    proc_bieter_5 = proc_bieter_5/100

    faktor_block_2= st.number_input('Faktor Block 2 Grundkörper', value  = 100)
    faktor_block_2 = faktor_block_2/100

    faktor_block_5= st.number_input('Faktor Block 5 Ersatzteile', value = 100)
    faktor_block_5 = faktor_block_5/100



    df_sum_temp = pd.DataFrame()

    for i in list(data.keys())[1:]:
        if i in ['Block 1', 'Block 2', 'Block 3', 'Block 4', 'Block 5']:
            print(i)
            counter = counter+1
            w_matr = pd.read_excel('0.2-Wertungsmatrix 21FEA52724 RV FT EUGEN Bieter VR.xlsm', sheet_name =i, header=0)            
            w_matr['OZ'] = w_matr['OZ'].astype(str)
            w_matr['OZ'] = w_matr['OZ'].str.replace('.', '')
            w_matr['OZ'] = w_matr['OZ'].astype(float)

            block_2 = pd.merge(w_matr, df_preis, how='left', on = 'OZ')
            block_2['Einheitspreis'] = block_2['Einheitspreis'] * proc_bieter_2
            block_2['Faktor Block']= 1
            block_2['Faktor x Preis'] = block_2['Einheitspreis'] * block_2['Wichtungs-\nFaktor'] * block_2['Faktor Block']
            block_2['Einheitspreis']=block_2['Einheitspreis'].fillna(0)
            block_2['Faktor x Preis']= block_2['Faktor x Preis'].fillna(0)
            block_2.append(block_2[['Einheitspreis', 'Faktor x Preis']].sum(), ignore_index=True)

            df_sum_temp = df_sum_temp.append(block_2[['Einheitspreis', 'Faktor x Preis']].sum(), ignore_index=True)
            df_sum_temp['% vom Einheitspreis'] =proc_bieter_2 *100
            df_sum_temp['Faktor Block'] = block_2['Faktor Block'][0]
            df_sum_temp['Bieter'] =2
            df_sum_temp['Block'] =i
            df_sum = pd.concat([df_sum, df_sum_temp])
    #resul = pd.pivot_table(df_sum, values=['Einheitspreis', 'Faktor x Preis'], index=[ 'Bieter','Block',  '% vom Einheitspreis'],   aggfunc='sum', fill_value=None, margins=False, dropna=True)
    #resul.reset_index(inplace=True)
    #resul = resul.sort_values('Bieter', axis=0, ascending=True)







with col3:

    proc_bieter_3= st.number_input('% für Bieter 3', value =  60)
    proc_bieter_3 = proc_bieter_3/100

    faktor_block_3= st.number_input('Faktor Block 3 Dienstleistung', value = 100)
    faktor_block_3 = faktor_block_3/100


    #Anbieter 3

    df_sum_temp = pd.DataFrame()

    for i in list(data.keys())[1:]:
        if i in ['Block 1', 'Block 2', 'Block 3', 'Block 4', 'Block 5']:
            print(i)
            counter = counter+1
            w_matr = pd.read_excel('0.2-Wertungsmatrix 21FEA52724 RV FT EUGEN Bieter VR.xlsm', sheet_name =i, header=0)            
            w_matr['OZ'] = w_matr['OZ'].astype(str)
            w_matr['OZ'] = w_matr['OZ'].str.replace('.', '')
            w_matr['OZ'] = w_matr['OZ'].astype(float)

            block_3 = pd.merge(w_matr, df_preis, how='left', on = 'OZ')
            block_3['Einheitspreis'] = block_3['Einheitspreis'] * proc_bieter_3
            block_3['Faktor Block']= 1
            block_3['Faktor x Preis'] = block_3['Einheitspreis'] * block_2['Wichtungs-\nFaktor'] * block_3['Faktor Block']
            block_3['Einheitspreis']=block_3['Einheitspreis'].fillna(0)
            block_3['Faktor x Preis']= block_3['Faktor x Preis'].fillna(0)
            block_3.append(block_3[['Einheitspreis', 'Faktor x Preis']].sum(), ignore_index=True)

            df_sum_temp = df_sum_temp.append(block_3[['Einheitspreis', 'Faktor x Preis']].sum(), ignore_index=True)
            df_sum_temp['% vom Einheitspreis'] =proc_bieter_3 *100
            df_sum_temp['Faktor Block'] = block_3['Faktor Block'][0]
            df_sum_temp['Bieter'] =3
            df_sum_temp['Block'] =i
            df_sum = pd.concat([df_sum, df_sum_temp])

#Anbieter 4

df_sum_temp = pd.DataFrame()

for i in list(data.keys())[1:]:
    if i in ['Block 1', 'Block 2', 'Block 3', 'Block 4', 'Block 5']:
        print(i)
        counter = counter+1
        w_matr = pd.read_excel('0.2-Wertungsmatrix 21FEA52724 RV FT EUGEN Bieter VR.xlsm', sheet_name =i, header=0)            
        w_matr['OZ'] = w_matr['OZ'].astype(str)
        w_matr['OZ'] = w_matr['OZ'].str.replace('.', '')
        w_matr['OZ'] = w_matr['OZ'].astype(float)

        block_4 = pd.merge(w_matr, df_preis, how='left', on = 'OZ')
        block_4['Einheitspreis'] = block_4['Einheitspreis'] * proc_bieter_4
        block_4['Faktor Block']= 1
        block_4['Faktor x Preis'] = block_4['Einheitspreis'] * block_2['Wichtungs-\nFaktor'] * block_3['Faktor Block']
        block_4['Einheitspreis']=block_4['Einheitspreis'].fillna(0)
        block_4['Faktor x Preis']= block_4['Faktor x Preis'].fillna(0)
        block_4.append(block_4[['Einheitspreis', 'Faktor x Preis']].sum(), ignore_index=True)

        df_sum_temp = df_sum_temp.append(block_4[['Einheitspreis', 'Faktor x Preis']].sum(), ignore_index=True)
        df_sum_temp['% vom Einheitspreis'] =proc_bieter_4 *100
        df_sum_temp['Faktor Block'] = block_4['Faktor Block'][0]
        df_sum_temp['Bieter'] =4
        df_sum_temp['Block'] =i
        df_sum = pd.concat([df_sum, df_sum_temp])







with col2:
    counter =0
    #proc_bieter_5= st.number_input('% für Bieter 5', value = 100)
    #proc_bieter_5 = proc_bieter_5/100
    df_sum_temp = pd.DataFrame()

    for i in list(data.keys())[1:]:
        if i in ['Block 1', 'Block 2', 'Block 3', 'Block 4', 'Block 5']:
            counter = counter+1
            w_matr = pd.read_excel('0.2-Wertungsmatrix 21FEA52724 RV FT EUGEN Bieter VR.xlsm', sheet_name =i, header=0)            

            w_matr['OZ'] = w_matr['OZ'].astype(str)


            w_matr['OZ'] = w_matr['OZ'].str.replace('.', '')



            w_matr['OZ'] = w_matr['OZ'].astype(float)

            block_5 = pd.merge(w_matr, df_preis, how='left', on = 'OZ')
            block_5['Einheitspreis'] = block_5['Einheitspreis'] * proc_bieter_5

            if i == 'Block 1':
                block_5['Faktor Block'] = faktor_block_1
            elif i == 'Block 2':
                block_5['Faktor Block'] = faktor_block_2
            elif i == 'Block 3':
                block_5['Faktor Block'] = faktor_block_3
            elif i == 'Block 4':
                block_5['Faktor Block'] = faktor_block_4
            elif i == 'Block 5':
                block_5['Faktor Block'] = faktor_block_5

            block_5['Faktor x Preis'] = block_5['Einheitspreis'] * block_5['Wichtungs-\nFaktor'] * block_5['Faktor Block']
            block_5['Einheitspreis']=block_5['Einheitspreis'].fillna(0)
            block_5['Faktor x Preis']= block_5['Faktor x Preis'].fillna(0)

            block_5.append(block_5[['Einheitspreis', 'Faktor x Preis']].sum(), ignore_index=True)
            #block_1['Preis'] = block_1['Einheitspreis']
            #block_1 = block_1.drop('Einheitspreis', axis=1)



            df_sum_temp = df_sum_temp.append(block_5[['Einheitspreis', 'Faktor x Preis']].sum(), ignore_index=True)
            #df_sum_temp['Faktor'] = block_1['Faktor x Preis'] / block_1['Einheitspreis']
            #df_sum_temp['Faktor'] = block_2['Wichtungs-\nFaktor']
            df_sum_temp['% vom Einheitspreis'] =proc_bieter_5 *100

            df_sum_temp['Bieter'] =5
            df_sum_temp['Faktor Block'] = block_5['Faktor Block'][0]
            df_sum_temp['Block'] =i
            df_sum = pd.concat([df_sum, df_sum_temp])
    resul = pd.pivot_table(df_sum, values=['Einheitspreis', 'Faktor x Preis'], index=['Bieter', 'Block', 'Faktor Block', '% vom Einheitspreis'],   aggfunc='sum', fill_value=None, margins=False, dropna=True)
    resul.reset_index(inplace=True)
    resul = resul.sort_values('Bieter', axis=0, ascending=True)
    resul_sum = resul.groupby('Bieter')[['Einheitspreis', 'Faktor x Preis']].sum().round(2)
    resul_sum.reset_index(inplace=True)
    resul_sum= resul_sum.sort_values('Faktor x Preis', axis=0, ascending=True)
st.title('Wertungsmatrix Summary')
st.table(resul_sum)

st.title('Details')
st.table(resul)

st.title('df_sum')
st.table(df_sum)

#col4, col5  =st.beta_columns(2)

#with col4:
writer = pd.ExcelWriter('wertungsmatrix_blocks.xlsx', engine='xlsxwriter')
for i in list(data.keys())[1:]:
    if i in ['Block 1', 'Block 2', 'Block 3', 'Block 4', 'Block 5']:
        w_matr = pd.read_excel('0.2-Wertungsmatrix 21FEA52724 RV FT EUGEN Bieter VR.xlsm', sheet_name =i, header=0)            

        w_matr['OZ'] = w_matr['OZ'].astype(str)


        w_matr['OZ'] = w_matr['OZ'].str.replace('.', '')



        w_matr['OZ'] = w_matr['OZ'].astype(float)

        block_ = pd.merge(w_matr, df_preis, how='left', on = 'OZ')
        block_['Einheitspreis'] = block_['Einheitspreis']
        block_ = block_.drop('Preis', axis=1)



        # Write each dataframe to a different worksheet.
        block_.to_excel(writer, sheet_name=i, index=False)





        st.title(i)
        st.table(block_)
# Close the Pandas Excel writer and output the Excel file.
writer.save()


#st.table(resul)
#st.table(df_sum)
