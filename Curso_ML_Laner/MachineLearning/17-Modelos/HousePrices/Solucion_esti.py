# -*- coding: utf-8 -*-

import os
import pandas as pd
import numpy as np
import cvxpy
from fancyimpute  import IterativeImputer 
from sklearn import linear_model
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
from sklearn.model_selection import train_test_split
from xgboost import plot_importance
from sklearn.preprocessing import StandardScaler

os.chdir(r"C:\Users\LENOVO\Documents\DataVM\CursoPythonCompleto\17-Modelos\HousePrices")
data = pd.read_csv("train.csv")

################### 1. ENTENDER EL DATASET ############################

"""
# Añadimos un resumen de los datos
SSubClass: Identifies the type of dwelling involved in the sale.	

        20	1-STORY 1946 & NEWER ALL STYLES
        30	1-STORY 1945 & OLDER
        40	1-STORY W/FINISHED ATTIC ALL AGES
        45	1-1/2 STORY - UNFINISHED ALL AGES
        50	1-1/2 STORY FINISHED ALL AGES
        60	2-STORY 1946 & NEWER
        70	2-STORY 1945 & OLDER
        75	2-1/2 STORY ALL AGES
        80	SPLIT OR MULTI-LEVEL
        85	SPLIT FOYER
        90	DUPLEX - ALL STYLES AND AGES
       120	1-STORY PUD (Planned Unit Development) - 1946 & NEWER
       150	1-1/2 STORY PUD - ALL AGES
       160	2-STORY PUD - 1946 & NEWER
       180	PUD - MULTILEVEL - INCL SPLIT LEV/FOYER
       190	2 FAMILY CONVERSION - ALL STYLES AND AGES

MSZoning: Identifies the general zoning classification of the sale.
		
       A	Agriculture
       C	Commercial
       FV	Floating Village Residential
       I	Industrial
       RH	Residential High Density
       RL	Residential Low Density
       RP	Residential Low Density Park 
       RM	Residential Medium Density
	
LotFrontage: Linear feet of street connected to property

LotArea: Lot size in square feet

Street: Type of road access to property

       Grvl	Gravel	
       Pave	Paved
       	
Alley: Type of alley access to property

       Grvl	Gravel
       Pave	Paved
       NA 	No alley access
		
LotShape: General shape of property

       Reg	Regular	
       IR1	Slightly irregular
       IR2	Moderately Irregular
       IR3	Irregular
       
LandContour: Flatness of the property

       Lvl	Near Flat/Level	
       Bnk	Banked - Quick and significant rise from street grade to building
       HLS	Hillside - Significant slope from side to side
       Low	Depression
		
Utilities: Type of utilities available
		
       AllPub	All public Utilities (E,G,W,& S)	
       NoSewr	Electricity, Gas, and Water (Septic Tank)
       NoSeWa	Electricity and Gas Only
       ELO	Electricity only	
	
LotConfig: Lot configuration

       Inside	Inside lot
       Corner	Corner lot
       CulDSac	Cul-de-sac
       FR2	Frontage on 2 sides of property
       FR3	Frontage on 3 sides of property
	
LandSlope: Slope of property
		
       Gtl	Gentle slope
       Mod	Moderate Slope	
       Sev	Severe Slope
	
Neighborhood: Physical locations within Ames city limits

       Blmngtn	Bloomington Heights
       Blueste	Bluestem
       BrDale	Briardale
       BrkSide	Brookside
       ClearCr	Clear Creek
       CollgCr	College Creek
       Crawfor	Crawford
       Edwards	Edwards
       Gilbert	Gilbert
       IDOTRR	Iowa DOT and Rail Road
       MeadowV	Meadow Village
       Mitchel	Mitchell
       Names	North Ames
       NoRidge	Northridge
       NPkVill	Northpark Villa
       NridgHt	Northridge Heights
       NWAmes	Northwest Ames
       OldTown	Old Town
       SWISU	South & West of Iowa State University
       Sawyer	Sawyer
       SawyerW	Sawyer West
       Somerst	Somerset
       StoneBr	Stone Brook
       Timber	Timberland
       Veenker	Veenker
			
Condition1: Proximity to various conditions
	
       Artery	Adjacent to arterial street
       Feedr	Adjacent to feeder street	
       Norm	Normal	
       RRNn	Within 200' of North-South Railroad
       RRAn	Adjacent to North-South Railroad
       PosN	Near positive off-site feature--park, greenbelt, etc.
       PosA	Adjacent to postive off-site feature
       RRNe	Within 200' of East-West Railroad
       RRAe	Adjacent to East-West Railroad
	
Condition2: Proximity to various conditions (if more than one is present)
		
       Artery	Adjacent to arterial street
       Feedr	Adjacent to feeder street	
       Norm	Normal	
       RRNn	Within 200' of North-South Railroad
       RRAn	Adjacent to North-South Railroad
       PosN	Near positive off-site feature--park, greenbelt, etc.
       PosA	Adjacent to postive off-site feature
       RRNe	Within 200' of East-West Railroad
       RRAe	Adjacent to East-West Railroad
	
BldgType: Type of dwelling
		
       1Fam	Single-family Detached	
       2FmCon	Two-family Conversion; originally built as one-family dwelling
       Duplx	Duplex
       TwnhsE	Townhouse End Unit
       TwnhsI	Townhouse Inside Unit
	
HouseStyle: Style of dwelling
	
       1Story	One story
       1.5Fin	One and one-half story: 2nd level finished
       1.5Unf	One and one-half story: 2nd level unfinished
       2Story	Two story
       2.5Fin	Two and one-half story: 2nd level finished
       2.5Unf	Two and one-half story: 2nd level unfinished
       SFoyer	Split Foyer
       SLvl	Split Level
	
OverallQual: Rates the overall material and finish of the house

       10	Very Excellent
       9	Excellent
       8	Very Good
       7	Good
       6	Above Average
       5	Average
       4	Below Average
       3	Fair
       2	Poor
       1	Very Poor
	
OverallCond: Rates the overall condition of the house

       10	Very Excellent
       9	Excellent
       8	Very Good
       7	Good
       6	Above Average	
       5	Average
       4	Below Average	
       3	Fair
       2	Poor
       1	Very Poor
		
YearBuilt: Original construction date

YearRemodAdd: Remodel date (same as construction date if no remodeling or additions)

RoofStyle: Type of roof

       Flat	Flat
       Gable	Gable
       Gambrel	Gabrel (Barn)
       Hip	Hip
       Mansard	Mansard
       Shed	Shed
		
RoofMatl: Roof material

       ClyTile	Clay or Tile
       CompShg	Standard (Composite) Shingle
       Membran	Membrane
       Metal	Metal
       Roll	Roll
       Tar&Grv	Gravel & Tar
       WdShake	Wood Shakes
       WdShngl	Wood Shingles
		
Exterior1st: Exterior covering on house

       AsbShng	Asbestos Shingles
       AsphShn	Asphalt Shingles
       BrkComm	Brick Common
       BrkFace	Brick Face
       CBlock	Cinder Block
       CemntBd	Cement Board
       HdBoard	Hard Board
       ImStucc	Imitation Stucco
       MetalSd	Metal Siding
       Other	Other
       Plywood	Plywood
       PreCast	PreCast	
       Stone	Stone
       Stucco	Stucco
       VinylSd	Vinyl Siding
       Wd Sdng	Wood Siding
       WdShing	Wood Shingles
	
Exterior2nd: Exterior covering on house (if more than one material)

       AsbShng	Asbestos Shingles
       AsphShn	Asphalt Shingles
       BrkComm	Brick Common
       BrkFace	Brick Face
       CBlock	Cinder Block
       CemntBd	Cement Board
       HdBoard	Hard Board
       ImStucc	Imitation Stucco
       MetalSd	Metal Siding
       Other	Other
       Plywood	Plywood
       PreCast	PreCast
       Stone	Stone
       Stucco	Stucco
       VinylSd	Vinyl Siding
       Wd Sdng	Wood Siding
       WdShing	Wood Shingles
	
MasVnrType: Masonry veneer type

       BrkCmn	Brick Common
       BrkFace	Brick Face
       CBlock	Cinder Block
       None	None
       Stone	Stone
	
MasVnrArea: Masonry veneer area in square feet

ExterQual: Evaluates the quality of the material on the exterior 
		
       Ex	Excellent
       Gd	Good
       TA	Average/Typical
       Fa	Fair
       Po	Poor
		
ExterCond: Evaluates the present condition of the material on the exterior
		
       Ex	Excellent
       Gd	Good
       TA	Average/Typical
       Fa	Fair
       Po	Poor
		
Foundation: Type of foundation
		
       BrkTil	Brick & Tile
       CBlock	Cinder Block
       PConc	Poured Contrete	
       Slab	Slab
       Stone	Stone
       Wood	Wood
		
BsmtQual: Evaluates the height of the basement

       Ex	Excellent (100+ inches)	
       Gd	Good (90-99 inches)
       TA	Typical (80-89 inches)
       Fa	Fair (70-79 inches)
       Po	Poor (<70 inches
       NA	No Basement
		
BsmtCond: Evaluates the general condition of the basement

       Ex	Excellent
       Gd	Good
       TA	Typical - slight dampness allowed
       Fa	Fair - dampness or some cracking or settling
       Po	Poor - Severe cracking, settling, or wetness
       NA	No Basement
	
BsmtExposure: Refers to walkout or garden level walls

       Gd	Good Exposure
       Av	Average Exposure (split levels or foyers typically score average or above)	
       Mn	Mimimum Exposure
       No	No Exposure
       NA	No Basement
	
BsmtFinType1: Rating of basement finished area

       GLQ	Good Living Quarters
       ALQ	Average Living Quarters
       BLQ	Below Average Living Quarters	
       Rec	Average Rec Room
       LwQ	Low Quality
       Unf	Unfinshed
       NA	No Basement
		
BsmtFinSF1: Type 1 finished square feet

BsmtFinType2: Rating of basement finished area (if multiple types)

       GLQ	Good Living Quarters
       ALQ	Average Living Quarters
       BLQ	Below Average Living Quarters	
       Rec	Average Rec Room
       LwQ	Low Quality
       Unf	Unfinshed
       NA	No Basement

BsmtFinSF2: Type 2 finished square feet

BsmtUnfSF: Unfinished square feet of basement area

TotalBsmtSF: Total square feet of basement area

Heating: Type of heating
		
       Floor	Floor Furnace
       GasA	Gas forced warm air furnace
       GasW	Gas hot water or steam heat
       Grav	Gravity furnace	
       OthW	Hot water or steam heat other than gas
       Wall	Wall furnace
		
HeatingQC: Heating quality and condition

       Ex	Excellent
       Gd	Good
       TA	Average/Typical
       Fa	Fair
       Po	Poor
		
CentralAir: Central air conditioning

       N	No
       Y	Yes
		
Electrical: Electrical system

       SBrkr	Standard Circuit Breakers & Romex
       FuseA	Fuse Box over 60 AMP and all Romex wiring (Average)	
       FuseF	60 AMP Fuse Box and mostly Romex wiring (Fair)
       FuseP	60 AMP Fuse Box and mostly knob & tube wiring (poor)
       Mix	Mixed
		
1stFlrSF: First Floor square feet
 
2ndFlrSF: Second floor square feet

LowQualFinSF: Low quality finished square feet (all floors)

GrLivArea: Above grade (ground) living area square feet

BsmtFullBath: Basement full bathrooms

BsmtHalfBath: Basement half bathrooms

FullBath: Full bathrooms above grade

HalfBath: Half baths above grade

Bedroom: Bedrooms above grade (does NOT include basement bedrooms)

Kitchen: Kitchens above grade

KitchenQual: Kitchen quality

       Ex	Excellent
       Gd	Good
       TA	Typical/Average
       Fa	Fair
       Po	Poor
       	
TotRmsAbvGrd: Total rooms above grade (does not include bathrooms)

Functional: Home functionality (Assume typical unless deductions are warranted)

       Typ	Typical Functionality
       Min1	Minor Deductions 1
       Min2	Minor Deductions 2
       Mod	Moderate Deductions
       Maj1	Major Deductions 1
       Maj2	Major Deductions 2
       Sev	Severely Damaged
       Sal	Salvage only
		
Fireplaces: Number of fireplaces

FireplaceQu: Fireplace quality

       Ex	Excellent - Exceptional Masonry Fireplace
       Gd	Good - Masonry Fireplace in main level
       TA	Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement
       Fa	Fair - Prefabricated Fireplace in basement
       Po	Poor - Ben Franklin Stove
       NA	No Fireplace
		
GarageType: Garage location
		
       2Types	More than one type of garage
       Attchd	Attached to home
       Basment	Basement Garage
       BuiltIn	Built-In (Garage part of house - typically has room above garage)
       CarPort	Car Port
       Detchd	Detached from home
       NA	No Garage
		
GarageYrBlt: Year garage was built
		
GarageFinish: Interior finish of the garage

       Fin	Finished
       RFn	Rough Finished	
       Unf	Unfinished
       NA	No Garage
		
GarageCars: Size of garage in car capacity

GarageArea: Size of garage in square feet

GarageQual: Garage quality

       Ex	Excellent
       Gd	Good
       TA	Typical/Average
       Fa	Fair
       Po	Poor
       NA	No Garage
		
GarageCond: Garage condition

       Ex	Excellent
       Gd	Good
       TA	Typical/Average
       Fa	Fair
       Po	Poor
       NA	No Garage
		
PavedDrive: Paved driveway

       Y	Paved 
       P	Partial Pavement
       N	Dirt/Gravel
		
WoodDeckSF: Wood deck area in square feet

OpenPorchSF: Open porch area in square feet

EnclosedPorch: Enclosed porch area in square feet

3SsnPorch: Three season porch area in square feet

ScreenPorch: Screen porch area in square feet

PoolArea: Pool area in square feet

PoolQC: Pool quality
		
       Ex	Excellent
       Gd	Good
       TA	Average/Typical
       Fa	Fair
       NA	No Pool
		
Fence: Fence quality
		
       GdPrv	Good Privacy
       MnPrv	Minimum Privacy
       GdWo	Good Wood
       MnWw	Minimum Wood/Wire
       NA	No Fence
	
MiscFeature: Miscellaneous feature not covered in other categories
		
       Elev	Elevator
       Gar2	2nd Garage (if not described in garage section)
       Othr	Other
       Shed	Shed (over 100 SF)
       TenC	Tennis Court
       NA	None
		
MiscVal: $Value of miscellaneous feature

MoSold: Month Sold (MM)

YrSold: Year Sold (YYYY)

SaleType: Type of sale
		
       WD 	Warranty Deed - Conventional
       CWD	Warranty Deed - Cash
       VWD	Warranty Deed - VA Loan
       New	Home just constructed and sold
       COD	Court Officer Deed/Estate
       Con	Contract 15% Down payment regular terms
       ConLw	Contract Low Down payment and low interest
       ConLI	Contract Low Interest
       ConLD	Contract Low Down
       Oth	Other
		
SaleCondition: Condition of sale

       Normal	Normal Sale
       Abnorml	Abnormal Sale -  trade, foreclosure, short sale
       AdjLand	Adjoining Land Purchase
       Alloca	Allocation - two linked properties with separate deeds, typically condo with a garage unit	
       Family	Sale between family members
       Partial	Home was not completed when last assessed (associated with New Homes)


"""

'''
el dataset tiene datos sobre diferentes características de casas (como el tamaño,
el tipo de material, la ubicación, si tiene garaje/piscina...) y el objetivo es 
predecir el precio de cada casa. Por lo tanto, se trata de un MODELO de REGRESIÓN.
'''

# Visión general de las características
AnalisisNumericas=data.describe() 


######################### 2. PREPROCESAMIENTO DE LOS DATOS #########################


### VALORES FALTANTES


# Observamos que hay variables con valores faltantes que indican cierta información.
# Lo primero es cambiar los NAs por la categoria que indican de acuerdo a los datos.
data.columns
data["Alley"]=data["Alley"].fillna("NO ALLEY ACCESS")
data["BsmtCond"]=data["BsmtCond"].fillna("NO BASEMENT")
data["BsmtExposure"]=data["BsmtExposure"].fillna("NO BASEMENT")
data["BsmtFinType1"]=data["BsmtFinType1"].fillna("NO BASEMENT")
data["BsmtFinType2"]=data["BsmtFinType2"].fillna("NO BASEMENT")
data["BsmtQual"]=data["BsmtQual"].fillna("NO BASEMENT")
data["FireplaceQu"]=data["FireplaceQu"].fillna("NO FIRE PLACE")
data["GarageType"]=data["GarageType"].fillna("NO GARAGE")
data["GarageQual"]=data["GarageQual"].fillna("NO GARAGE")
data["GarageCond"]=data["GarageCond"].fillna("NO GARAGE")
data["GarageFinish"]=data["GarageFinish"].fillna("NO GARAGE")
data["PoolQC"]=data["PoolQC"].fillna("NO POOL")
data["Fence"]=data["Fence"].fillna("NO FENCE")
data["MiscFeature"]=data["MiscFeature"].fillna("NONE")

# Una vez hecho esto pasamos a analizar los NAs como tal
data.isnull().any().any()

# Vemos que existen valores perdidos
# Realizamos un sumatorio para observar los NAs por columna.
Perdidos = data.isnull().sum()

'''
Los valores perdidos se concentran en:
LotFrontage(259), GarageYrBlt (81),MasVnrType (872), MasVnrArea (8) y Electrical (1)

Teniendo en cuenta que contamos con 81 variables, y la variable "MasVnrType" tiene 
aproximadamente el 60% de registros con valores faltantes, decidimos eliminarla.

Como unicamente hay un registro con la variable Electrical con NA la eliminamos.
También podríamos imputarla con la moda (ya que es categórica).
'''

del(data["MasVnrType"])
del(data["Electrical"])
del(data["Id"])

# Visualizamos los datos de No Garage
NoGarage = data[data["GarageType"]== "NO GARAGE"]
min(data["GarageYrBlt"])

'''
Vemos que los que NO tienen Garage coinciden con los que no tienen año.
En nuestro conjunto de datos el año mínimo es 1900. Luego decidimos convertir los
NAs referidos a los garages en 1800, ya que es un valor diferente pero no muy lejano
y puede servir al modelo.
'''

data["GarageYrBlt"]=data["GarageYrBlt"].fillna(1800)


'''
Al resto de los datos asumo que los valores perdidos son reales por lo que 
procedo a imputarlos con el Iterative Imputer, basado en modelado iterativo.
'''

# Identificamos las variables numéricas.
datoNum1=data.loc[:, data.dtypes == np.float64]
datoNum2=data.loc[:, data.dtypes == np.int64]

datoNum = pd.concat([datoNum1, datoNum2], axis=1)

# Identificamos las variables categóricas.
datoNoNum=data.loc[:, data.dtypes == object]

# Imputamos los valores perdidos de las variables numéricas
my_imputer = IterativeImputer()
datoNumcomp = my_imputer.fit_transform(datoNum)

datoNumcomp = pd.DataFrame(datoNumcomp)
datoNumcomp.columns = datoNum.columns

datos_completos= pd.concat([datoNoNum, datoNumcomp], axis=1)




### CORRELACION:
    
correlacion = datoNum.corr()
# Filtrar las filas donde la correlación con la variable objetivo es mayor a 0.6
filas_filtradas = correlacion[correlacion['SalePrice'] > 0.6].index




### CREAR NUEVAS VARIABLES:
    
# Procedemos a enriquecer los datos añadiendo nuevas variables.
datos_completos.columns

# Creamos una nueva columna llamada 'Crisis' para indicar si la venta ocurrió durante o 
# después de la crisis financiera de 2008.
datos_completos["Crisis"] = "NO"
datos_completos["Crisis"][datos_completos["YrSold"]>2007] = "SI"

# Creamos una nueva columna llamada 'TiempoPasado', que calcula el tiempo transcurrido desde la 
# última remodelación hasta el año de venta de la vivienda.
datos_completos["TiempoPasado"] = datos_completos["YrSold"] - datos_completos["YearRemodAdd"]




### TRANSFORMACIÓN DE LOS DATOS:
    
# Procedemos a binominalizar las variables categoricas.
datos_completos = pd.get_dummies(datos_completos, prefix=None, prefix_sep='_', dummy_na=False, columns=None, sparse=False, drop_first=False, dtype=None)


datos_completos.to_csv("datos_completos.csv", index = False)



################################## 3. ENTRENAR LOS MODELOS #####################################

### DIVISIÓN DE DATOS:
    
 # Seleccionamos la variable objetivo y las explicativas
y=datos_completos['SalePrice']
X = datos_completos.drop(['SalePrice'], axis = 1)

# Realizamos la particion dejando un 75% para entrenar y un 25% de test.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)



############# 3.1 REGRESION LINEAL 

regr = linear_model.LinearRegression()

# Entrenamos y evaluamos con los datos de train
regr.fit(X_train, y_train)

# Evaluamos con los datos de test
regr.score(X_test,y_test)


# Utilizamos la validacion cruzada
scores = cross_val_score(regr, X, y, cv=5)
scores
scores_cv_lr = scores.mean()
scores_cv_lr



############# 3.2 ARBOL DE DECISIÓN

arbol = DecisionTreeRegressor(criterion='squared_error', max_depth=8, max_features=None, max_leaf_nodes=None,min_impurity_decrease=0.0,min_samples_leaf=10, min_samples_split=2, min_weight_fraction_leaf=0.0, random_state=42, splitter='best')

# Entrenamos con los datos de train
arbol=arbol.fit(X_train, y_train)

# Evaluamos con los datos de test
arbol.score(X_test, y_test)

# Utilizamos la validacion cruzada
scores = cross_val_score(arbol, X, y, cv=5)
scores
scores_cv_tree = scores.mean()
scores_cv_tree



############# 3.3 RANDOM FOREST

RF= RandomForestRegressor(n_estimators=500, criterion='squared_error' ,max_features='sqrt' ,max_depth=500, min_samples_split=5, min_samples_leaf=3, max_leaf_nodes=None,min_impurity_decrease=0, bootstrap=True, oob_score=True, n_jobs=1, random_state=42, verbose=0, warm_start=False)

# Entrenamos con los datos de train
clf = RF.fit(X_train,y_train)

# Evaluamos con los datos de test
RF.score(X_test,y_test)

# Utilizamos la validacion cruzada
scores = cross_val_score(RF, X, y, cv=5)
scores
score_cv_rf = scores.mean()
score_cv_rf



############# 3.4 XGBOOST

xgb_model = xgb.XGBRegressor(base_score=1, colsample_bylevel=0.8, colsample_bytree=0.8, gamma=0.4, learning_rate=0.1, max_delta_step=0, max_depth=3, min_child_weight=1, missing=1, n_estimators=200, objective='reg:squarederror', reg_alpha=0.8, reg_lambda=0.5, scale_pos_weight=1, seed=42, subsample=1)

# Entrenamos con los datos de train
modeloxgb = xgb_model.fit(X_train,y_train)

# Evaluamos con los datos de test
xgb_model.score(X_test,y_test)

# Utilizamos la validacion cruzada
scores = cross_val_score(xgb_model, X, y, cv=5)
scores
score_cv_xgb = scores.mean()
score_cv_xgb


# Imprimimos por pantalla los resultados de los cuatro modelos

print(f"R2 score en regresion lineal: {scores_cv_lr:.4f}")
print(f"R2 score en arbol de decisión: {scores_cv_tree:.4f}")
print(f"R2 score en random forest: {score_cv_rf:.4f}")
print(f"R2 score en xgboost: {score_cv_xgb:.4f}")


'''
Observamos que el mejor modelo es el XGBOOST. Después de entrenarlo con 298 variables, 
voy a analizar la importancia de las variables. Una opción podría ser entrenar 
de nuevo el modelo basándonos en las importancias derivadas del modelo, y entrenar
nuevamente el modelo con este conjunto reducido de características, y observar como
cambia la métrica.
'''

############# 3.4.1 XGBOOST (REDUCIDO)


# IMPORTANCIA DE LAS CARACTERÍSTICAS
importancias = modeloxgb.feature_importances_

# Mostrar las características ordenadas por importancia
importancia_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importancias
}).sort_values(by="Importance", ascending=False)


# Filtrar las características con importancia distinta de cero
caracteristicas_importantes = importancia_df[importancia_df["Importance"] > 0]

#############
# filas_filtradas son las variables con una correlacion mayor a 0.6 con la variable objetivo
variables = caracteristicas_importantes['Feature'].isin(filas_filtradas)

# Filtrar las coincidencias
coincidencias = caracteristicas_importantes[variables]

'''
Se observa que las 6 variables con mayor correlación con la variable objetivo 
coinciden entre las más importantes identificadas por el modelo para realizar la 
predicción, lo cual tiene sentido, ya que una alta correlación suele estar asociada 
con una mayor influencia en el desempeño del modelo.
'''
#############

# Crear una lista de las características importantes
caracteristicas_seleccionadas = caracteristicas_importantes["Feature"].values.tolist()

# Añadimos la variable objetico a la lista de características seleccionadas
caracteristicas_seleccionadas.append("SalePrice")

# Seleccionar las columnas importantes del DataFrame original
datos_completos_reducido = datos_completos[caracteristicas_seleccionadas]




# Volvemos a hacer la DIVISIÓN DE LOS DATOS
y_reducido=datos_completos_reducido['SalePrice']
X_reducido = datos_completos_reducido.drop(['SalePrice'], axis = 1)

X_train_red, X_test_red, y_train_red, y_test_red = train_test_split(X_reducido, y_reducido, test_size=0.25, random_state=42)




# ENTRENAMOS con los datos de train
modeloxgb = xgb_model.fit(X_train_red,y_train_red)

# Evaluamos con los datos de test
xgb_model.score(X_test_red,y_test_red)

# Utilizamos la validacion cruzada
scores = cross_val_score(xgb_model, X_reducido, y_reducido, cv=5)
scores
score_cv_xgb_red = scores.mean()
score_cv_xgb_red

print(f"R2 score en xgboost: {score_cv_xgb:.4f}")
print(f"R2 score en xgboost reducido: {score_cv_xgb_red:.4f}")


'''
Estos resultados indican que las métricas obtenidas en ambos casos son muy similares, 
a pesar de la reducción significativa en el número de variables. Esto sugiere que las
variables seleccionadas son las más relevantes para predecir la variable objetivo, y 
que eliminar las variables menos importantes no ha afectado de manera significativa el 
rendimiento del modelo.

Por lo tanto, ya que el modelo reducido XGBoost ha producido un rendimiento 
casi idéntico al modelo completo pero con una cantidad significativamente menor 
de variables (casi 150 variables menos), nuestro modelo final será el XGBoost reducido. 
Esto no solo mejora la eficiencia computacional sino que también reduce el riesgo de 
sobreajuste al trabajar con un conjunto de datos más pequeño pero igualmente potente.
'''

############################

### PROBAMOS NORMALIZANDO LAS VARIABLES

XX = datos_completos_reducido.drop("SalePrice", axis=1)  
yy = datos_completos_reducido["SalePrice"] 


XX_num1=XX.loc[:, XX.dtypes == np.float64]
XX_num2=XX.loc[:, XX.dtypes == np.int64]
XX_num = pd.concat([XX_num1, XX_num2], axis=1)

XX_Nonum=XX.loc[:, XX.dtypes == bool]


# Estandarizamos las variables numericas
scaler = StandardScaler()
XX_num_estandarizado = scaler.fit_transform(XX_num)

XX_num_estandarizado=pd.DataFrame(XX_num_estandarizado)
XX_num_estandarizado.columns=XX_num.columns

X_estandarizado = pd.concat([XX_num_estandarizado, XX_Nonum], axis=1)


# Dividimos los datos 
X_train_est, X_test_est, y_train_est, y_test_est = train_test_split(X_estandarizado, y, test_size=0.2, random_state=42)

# Entrenamos
xgb_model.fit(X_train_est, y_train_est)

# Evaluamos el modelo
r2_score_test = xgb_model.score(X_test_est, y_test_est)

# Utilizamos la validacion cruzada
scores = cross_val_score(xgb_model, X_estandarizado, y, cv=5)
scores
score_cv_xgb_red_est = scores.mean()
score_cv_xgb_red_est

print(f"R2 Score en xgboost reducido: {score_cv_xgb_red:.4f}")
print(f"R2 Score en xgboost reducido normalizado: {score_cv_xgb_red_est:.4f}")


'''
El modelo XGBoost funciona bastante bien tanto si normalizas los datos como si 
no, lo cual es común en los modelos de árboles de decisión, ya que no se ve tan 
afectado por las diferencias de escala entre las variables. Como XGBoost maneja 
bien las variables con escalas distintas y es resistente a los outliers, no es 
estrictamente necesario normalizar en este caso los datos. 
'''



############################### 4. PREDICCIONES SOBRE EL TEST #########################
# Procedemos a realizar las predicciones sobre test con el mejor modelo

test = pd.read_csv("test.csv")


################# Aplicamos el MISMO TRATAMIENTO a los datos de test

## 1

test["Alley"]=test["Alley"].fillna("NO ALLEY ACCESS")
test["BsmtCond"]=test["BsmtCond"].fillna("NO BASEMENT")
test["BsmtExposure"]=test["BsmtExposure"].fillna("NO BASEMENT")
test["BsmtFinType1"]=test["BsmtFinType1"].fillna("NO BASEMENT")
test["BsmtFinType2"]=test["BsmtFinType2"].fillna("NO BASEMENT")
test["BsmtQual"]=test["BsmtQual"].fillna("NO BASEMENT")
test["FireplaceQu"]=test["FireplaceQu"].fillna("NO FIRE PLACE")
test["GarageType"]=test["GarageType"].fillna("NO GARAGE")
test["GarageQual"]=test["GarageQual"].fillna("NO GARAGE")
test["GarageCond"]=test["GarageCond"].fillna("NO GARAGE")
test["GarageFinish"]=test["GarageFinish"].fillna("NO GARAGE")
test["PoolQC"]=test["PoolQC"].fillna("NO POOL")
test["Fence"]=test["Fence"].fillna("NO FENCE")
test["MiscFeature"]=test["MiscFeature"].fillna("NONE")

## 2

test["GarageYrBlt"]=test["GarageYrBlt"].fillna(1800)

## 3

del(test["MasVnrType"])
del(test["Electrical"])
del(test["Id"])

## 4

datoNum1=test.loc[:, test.dtypes == np.float64]
datoNum2=test.loc[:, test.dtypes == np.int64]
datoNum = pd.concat([datoNum1, datoNum2], axis=1)
datoNoNum=test.loc[:, test.dtypes == object]


my_imputer = IterativeImputer()
datoNumcomp = my_imputer.fit_transform(datoNum)
datoNumcomp=pd.DataFrame(datoNumcomp)

datoNumcomp.columns = datoNum.columns
datos_completos_test= pd.concat([datoNoNum, datoNumcomp], axis=1)

## 5

datos_completos_test.columns
datos_completos_test["Crisis"] = "NO"
datos_completos_test["Crisis"][datos_completos_test["YrSold"]>2007] = "SI"

datos_completos_test["TiempoPasado"] = datos_completos_test["YrSold"] - datos_completos_test["YearRemodAdd"]


## 6

datos_completos_test = pd.get_dummies(datos_completos_test, prefix=None, prefix_sep='_', dummy_na=False, columns=None, sparse=False, drop_first=False, dtype=None)

# (tiene 279 columnas cuando la nuestra original eran 297)



################################# PREDICCIÓN 

prediccion = modeloxgb.predict(datos_completos_test)

# Da error porque hay diferentes variables
# Obtener las columnas del DataFrame de entrenamiento (el que se usó para entrenar el modelo)
columnas_entrenamiento = datos_completos_reducido.columns

# Filtrar el conjunto de prueba para que contenga solo las columnas que están en el conjunto de entrenamiento
datos_completos_test2 = datos_completos_test[columnas_entrenamiento.intersection(datos_completos_test.columns)]


# Buscar las columnas que están en el conjunto de entrenamiento pero no en el conjunto de prueba. Inicializarlas como 0
Diferentes=datos_completos_reducido[(datos_completos_reducido.columns.difference(datos_completos_test2.columns))]

Diferentes[:] = 0
Diferentes=Diferentes[Diferentes.index.isin(datos_completos_test2.index)]

datos_completos_test_2 = pd.concat([datos_completos_test2, Diferentes], axis=1)


del(datos_completos_test_2["SalePrice"])

# Volvemos a sacar las predicciones
prediccion = modeloxgb.predict(datos_completos_test_2)


# Da error por que las columnas no siguen el mismo orden
# Las ordenamos
datos_completos2 = datos_completos_reducido.copy()
del(datos_completos2["SalePrice"])

datos_completos_test_2.columns

df3 = datos_completos_test_2[datos_completos2.columns]

prediccion = modeloxgb.predict(df3)



############################# Ponemos las predicciones en GENDER SUBMISSION

submit = pd.read_csv("sample_submission.csv")

submit["SalePrice"] = prediccion

submit.to_csv("Subir.csv", index = False)