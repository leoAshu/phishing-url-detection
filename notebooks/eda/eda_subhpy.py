import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
# importing required packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("redgrid")

data = pd.read_csv('C:\\Users\\Checkout\\Desktop\\data.csv')

data.head()


data.shape


# distribution of datapoints into respective class labelsa 
print(data['Sentiment'].value_counts())

# plotting the class distribution after droping duplicates
plt.figure(dpi=110)
chart = sns.countplot(x="Sentiment", data=data, palette="Set2")
axes = chart.axes
axes.set_title('Class_Circulation')
axes.set_xlabel('Sentiment')
plt.show()


# finding duplicate sentences
data[data['Sentence'].duplicated()]

# extracting indices of duplicate sentences
duplicate_indices = data[data['Sentence'].duplicated()].index.to_list()

# printing each set of duplicate sentences
for index in duplicate_indices:
    print(data[data['Sentence'] == data['Sentence'].loc[index]])
    print()


# dropping the duplicate sentences with "neutral" sentiment
for index in duplicate_indices:
    temp = data[data['Sentence'] == data['Sentence'].loc[index]]
    dup_idx = temp[temp['Sentiment'] == 'neutral'].index[0]
    data = data.drop(index=dup_idx)

# resetting the index
data.reset_index()
    
# verifying if duplicate sentences are dropped
data[data['Sentence'].duplicated()]


# updated distribution of datapoints into respective class labels
print(data['Sentiment'].value_counts())

# plotting the class distribution after droping duplicates
plt.figure(dpi=110)
chart = sns.countplot(x="Sentiment", data=data, palette="Set2")
axes = chart.axes
axes.set_title('Class Distribution - Updated')
axes.set_xlabel('Sentiment')
plt.show()


# counting null values in the dataset
data.isnull().sum()

# save the cleaned dataset
data.to_csv('C:\\Users\\Checkout\\Desktop\\data.csv', index=False)


