import matplotlib.pyplot as plt

# データの準備
technologies = ['AWS', 'Azure', 'Google Cloud', 'IBM Cloud', 'Oracle Cloud', 'Salesforce', 'VMware Cloud', 'Alibaba Cloud', 'DigitalOcean', 'Heroku', 'Fry.io', 'Render']
release_year = [2006, 2010, 2008, 2011, 2012, 1999, 2010, 2009, 2011, 2007, 2019, 2018]
cutting_edge_score = [9.8, 9.6, 9.4, 8.5, 7.8, 8.0, 7.5, 7.9, 8.2, 8.4, 8.9, 9.0]

# 散布図のプロット
plt.figure(figsize=(10, 8))

# 色分け
experienced = ['AWS', 'Render']
colors = ['red' if tech in experienced else 'blue' for tech in technologies]

# プロットとラベル追加
for i, tech in enumerate(technologies):
    plt.scatter(release_year[i], cutting_edge_score[i], color=colors[i])
    plt.text(release_year[i], cutting_edge_score[i], tech, fontsize=9)

# グラフのラベル
plt.xlabel('Release Year')
plt.ylabel('Cutting Edge Score (1-10)')
plt.title('Cutting Edge Score vs. Release Year of Cloud Technologies')
plt.ylim(1, 10)  # Y軸の範囲を1～10に設定

# 凡例の追加
red_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Experienced')
blue_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='UnExperienced')
plt.legend(handles=[red_patch, blue_patch])

plt.grid(True)
plt.savefig('cloud_scatter_plot.png')
plt.show()

