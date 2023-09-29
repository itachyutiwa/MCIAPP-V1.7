import pandas as pd

files = [
    "E:/CONTROLES DELEGUES MCI-CARE CI/SN BENIN/SN ASCOMA BENEFS A 2022.xlsx",
    "E:/CONTROLES DELEGUES MCI-CARE CI/SN BENIN/COTIS BN SEM01 2021.xlsx",
    "E:/CONTROLES DELEGUES MCI-CARE CI/SN BENINSN/CONSOMMATION SEM01 2021 BJ.xlsx"
]
df1 = pd.read_excel("E:\CONTROLES DELEGUES MCI-CARE CI\SN BENIN\CONSOMMATION SEM01 2021 BJ.xlsx")
#df2 = pd.read_excel(files[1])
#df3 = pd.read_excel(files[2])
# Fonction pour convertir une chaîne en camel case sans espaces


def to_camel_case(column_name):
    # Supprimez les espaces et les underscores et divisez la chaîne en mots
    words = column_name.replace(" ", "_").replace("_", " ").split()
    camel_case_name = words[0].lower() + ''.join(word.capitalize()
                                                 for word in words[1:])
    return camel_case_name


# Renommez les colonnes de la DataFrame en utilisant la fonction to_camel_case
df1.columns = [to_camel_case(column) for column in df1.columns]


print(df1.columns)
