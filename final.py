import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv('C:/Users/Colin/Downloads/team_stats_2003_2023.csv')

# Sidebar for filtering data
st.sidebar.title('Filter Data')
df_2023 = df[df['year'] == 2023]

# Plotting
plt.figure(figsize=(10, 6))

# Scatter plot of turnovers vs points allowed
plt.scatter(df_2023['turnovers'], df_2023['points_opp'], alpha=0.7)
plt.title('Turnovers vs Points Allowed for 2023 Teams')
plt.xlabel('Turnovers')
plt.ylabel('Points Allowed')
plt.grid(True)

st.pyplot(plt)


# Bar plot of winning percentage by year for selected teams
st.sidebar.title('Filter Teams for Winning Percentage')
selected_teams = st.sidebar.multiselect('Select Teams', df['team'].unique(), default=df['team'].unique())
filtered_team_df = df[df['team'].isin(selected_teams)]
grouped_df = filtered_team_df.groupby(['year', 'team']).mean()['win_loss_perc'].unstack()
st.subheader('Winning Percentage by Year for Selected Teams')
plt.figure(figsize=(12, 8))
for i, team in enumerate(grouped_df.columns):
    plt.bar(grouped_df.index + 0.2 * i, grouped_df[team], width=0.2, label=team)
plt.title('Winning Percentage by Year')
plt.xlabel('Year')
plt.ylabel('Winning Percentage')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
st.pyplot(plt)

# Scatter plot of passing yards vs rushing yards for selected teams
st.sidebar.title('Filter Teams for Passing and Rushing Yards')
selected_teams = st.sidebar.multiselect('Select Teams', ['All'] + list(df['team'].unique()), default=['All'])
filtered_team_df = df[df['team'].isin(selected_teams)]
filtered_team_df = filtered_team_df[filtered_team_df['wins'] >= 10]
st.subheader('Passing Yards per Win for Selected Teams')
plt.figure(figsize=(12, 8))
for team in filtered_team_df['team'].unique():
    team_data = filtered_team_df[filtered_team_df['team'] == team]
    team_data['yards_per_win'] = team_data['pass_yds'] / team_data['wins']  # Calculate yards per win
    plt.plot(team_data['year'], team_data['yards_per_win'], marker='o', label=team)
plt.title('NFL Team Stats')
plt.xlabel('Year')
plt.ylabel('Passing Yards per Win')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.xticks(rotation=45)
st.pyplot(plt)

# Bar plot of passing yards by team for the selected year
st.sidebar.title('Filter Year for Passing Yards')
selected_year = st.sidebar.number_input('Select Year', min_value=2003, max_value=2023, value=2023)
filtered_df = df[df['year'] == selected_year]
filtered_df = filtered_df.sort_values(by='pass_yds', ascending=False)
st.subheader(f'Passing Yards by Team in {selected_year}')
plt.figure(figsize=(10, 6))
plt.bar(filtered_df['team'], filtered_df['pass_yds'])
plt.title(f'Passing Yards by Team in {selected_year}')
plt.xlabel('Team')
plt.ylabel('Passing Yards')
plt.xticks(rotation=45, ha='right')
median_pass_yards = filtered_df['pass_yds'].median()
plt.axhline(y=median_pass_yards, color='r', linestyle='--', label='Median Passing Yards')
plt.legend()
plt.tight_layout()
st.pyplot(plt)

selected_year = st.sidebar.slider('Select Year', min_value=2003, max_value=2023, value=2023)

# Filter data based on selected year
filtered_df = df[df['year'] == selected_year]

# Plotting
plt.figure(figsize=(10, 6))

# Scatter plot of passing yards vs rushing yards
plt.scatter(filtered_df['pass_yds'], filtered_df['rush_yds'], alpha=0.7)
plt.title(f'Passing Yards vs Rushing Yards in {selected_year}')
plt.xlabel('Passing Yards')
plt.ylabel('Rushing Yards')
plt.grid(True)

st.pyplot(plt)

