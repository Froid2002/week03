# -*- coding: utf-8 -*-

import seaborn as sns
import matplotlib.pyplot as plt
import os

# Create week04 directory if it doesn't exist to avoid errors
if not os.path.exists('./week04'):
    os.makedirs('./week04')

# Load the dataset from seaborn library
# I am using the standard 'tips' data for this practice
df_tips = sns.load_dataset('tips')

# Check the first few rows to see the data structure
print(df_tips.head())
df_tips.info()

# --- PART 1: Categorical Plots ---
# Creating a figure with 2 areas (subplots)
my_fig1 = plt.figure(figsize=(15, 5))
plot1 = my_fig1.add_subplot(1, 2, 1)
plot2 = my_fig1.add_subplot(1, 2, 2)

#Drawing stripplot to see the points by day
sns.stripplot(x='day', y='tip', hue='sex', data=df_tips, alpha=0.6, ax=plot1)

#Swarmplot is similar but points don't overlap too much
sns.swarmplot(x='day', y='tip', hue='sex', data=df_tips, palette='muted', alpha=0.7, ax=plot2)

#Adding titles to understand each plot
plot1.set_title('Strip Plot: Tips vs Day')
plot2.set_title('Swarm Plot: Tips vs Day')
plt.savefig('./week04/Seaborn_Figure01.jpg')


#PART 2: Frequency Plots (Counting)
my_fig2 = plt.figure(figsize=(15, 5))
count_ax1 = my_fig2.add_subplot(1, 2, 1)
count_ax2 = my_fig2.add_subplot(1, 2, 2)

#Just counting how many tips per time (Lunch or Dinner)
sns.countplot(x='time', data=df_tips, ax=count_ax1)

#Counting time but also separating by day with different colors
sns.countplot(x='time', hue='day', data=df_tips, palette='pastel', ax=count_ax2)

count_ax1.set_title('Simple Count by Time')
count_ax2.set_title('Count by Time and Day')
plt.savefig('./week04/Seaborn_Figure02.jpg')


#PART 3: Regression Plots
my_fig3 = plt.figure(figsize=(15, 5))
reg_ax1 = my_fig3.add_subplot(1, 2, 1)
reg_ax2 = my_fig3.add_subplot(1, 2, 2)

#Plotting the bill vs tip with a trend line
sns.regplot(x='total_bill', y='tip', data=df_tips, color='green', scatter_kws={'s': 40, 'alpha': 0.4}, ax=reg_ax1)

# Same plot but without the trend line (fit_reg=False)
sns.regplot(x='total_bill', y='tip', data=df_tips, color='red', fit_reg=False, ax=reg_ax2)

my_fig3.suptitle('Checking Relation between Bill and Tips', fontsize=14)
plt.savefig('./week04/Seaborn_Figure03.jpg')


#PART 4: Distribution Plot
plt.figure()
# Using histplot to see the distribution of tips
sns.histplot(df_tips['tip'], bins=25, kde=True, color='orange')
plt.title('Distribution of Tip Amounts')
plt.savefig('./week04/Seaborn_Figure04.jpg')


#PART 5: Joint and Pair Plots
# Joint plot shows scatter and histogram together
sns.jointplot(x='size', y='tip', data=df_tips, kind='reg', color='purple')
plt.savefig('./week04/Seaborn_Figure05.jpg')

#Pairplot shows relations between all numeric columns
sns.pairplot(data=df_tips, hue='sex', palette='Set1')
plt.savefig('./week04/Seaborn_Figure06.jpg')

print("All figures saved in week04 folder.")

