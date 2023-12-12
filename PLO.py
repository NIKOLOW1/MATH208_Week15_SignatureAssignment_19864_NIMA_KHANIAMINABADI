{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\ri0\sl480\slmult1\partightenfactor0

\f0\fs24 \cf0 import pandas as pd\
from sklearn.linear_model import LinearRegression\
import matplotlib.pyplot as plt\
\
# Provided 'EDA' and 'label' values\
eda_values = [\
    6.769995, 6.769995, 6.769995, 6.769995, 6.769995, 6.769995, 6.769995, 6.769995, 6.805877, 6.805877,\
    # ... (other 'EDA' values)\
]\
label_values = [\
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2,\
    # ... (other 'label' values)\
]\
\
# Create a DataFrame combining 'EDA' and 'label' values\
data = pd.DataFrame(\{'EDA': eda_values, 'label': label_values\})\
\
# Extract X (independent variable) and Y (dependent variable) columns\
X = data['EDA'].values.reshape(-1, 1)  # Independent variable (EDA)\
Y = data['label'].values  # Dependent variable (label)\
\
# Create and fit the linear regression model\
model = LinearRegression()\
model.fit(X, Y)\
\
# Make predictions using the model\
Y_pred = model.predict(X)\
\
# Visualize the relationship between 'EDA' and 'label'\
plt.scatter(X, Y, color='blue', label='Actual')\
plt.plot(X, Y_pred, color='red', label='Predicted')\
plt.xlabel('EDA (Independent Variable)')\
plt.ylabel('Label (Dependent Variable)')\
plt.title('Linear Regression: EDA vs. Label')\
plt.legend()\
plt.show()\
\
# Display regression coefficients\
print('Intercept:', model.intercept_)\
print('Coefficient:', model.coef_[0])\
}