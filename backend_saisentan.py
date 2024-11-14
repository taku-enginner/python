import matplotlib.pyplot as plt

# データの準備
technologies = ['Node.js', 'Django', 'Flask', 'Ruby on Rails', 'Laravel', 'ASP.NET Core', 'Spring Boot', 'Express.js', 'FastAPI', 'Phoenix',
                'Perl', 'ColdFusion', 'CGI', 'WebObjects', 'Zope', 'Play Framework', 'Koa', 'Symfony', 'Meteor', 'Grails',
                'CodeIgniter', 'CakePHP']
release_year = [2009, 2005, 2010, 2004, 2011, 2016, 2014, 2010, 2018, 2015,
                1987, 1995, 1993, 1996, 1998, 2011, 2013, 2005, 2012, 2008,
                2006, 2005]
cutting_edge_score = [9.8, 8.0, 8.2, 7.8, 9.0, 8.5, 9.2, 9.5, 9.9, 8.7,
                      2.0, 3.0, 1.5, 2.5, 2.2, 7.5, 7.8, 7.5, 7.2, 7.4,
                      5.5, 5.8]

# 散布図のプロット
plt.figure(figsize=(10, 8))

# 色分け
experienced = ['Ruby on Rails']
colors = ['red' if tech in experienced else 'blue' for tech in technologies]

# プロットとラベル追加
for i, tech in enumerate(technologies):
    plt.scatter(release_year[i], cutting_edge_score[i], color=colors[i])
    plt.text(release_year[i], cutting_edge_score[i], tech, fontsize=9)

# グラフのラベル
plt.xlabel('Release Year')
plt.ylabel('Cutting Edge Score (1-10)')
plt.title('Cutting Edge Score vs. Release Year of Backend Technologies')
plt.ylim(1, 10)  # Y軸の範囲を1～10に設定

# 凡例の追加
red_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Experienced')
blue_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='UnExperienced')
plt.legend(handles=[red_patch, blue_patch])

plt.grid(True)
plt.savefig('backend_scatter_plot.png')
plt.show()

