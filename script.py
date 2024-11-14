import matplotlib.pyplot as plt

# データの準備
technologies = ['HTML/CSS', 'JavaScript', 'React', 'Vue.js', 'Angular', 'Svelte', 'Backbone.js', 'TypeScript',
                'WebAssembly', 'PWAs', 'SSR', 'SPA', 'GraphQL', 'Sass', 'Webpack', 'Less', 'Ember.js', 'jQuery',
                'Flash', 'HTML4', 'CSS2', 'SSI', 'Prototype.js']
release_year = [1993, 1995, 2013, 2014, 2010, 2016, 2010, 2012, 2017, 2015, 2014, 2010, 2015, 2006, 2012, 2009, 
                2011, 2006, 1996, 1997, 1998, 1995, 2006]
cutting_edge_score = [9.2, 9.4, 9.6, 9.4, 9.6, 9.5, 5, 9.2, 9.4, 9.6, 9.8, 10.0, 9.2, 7.2, 7.4, 5, 6, 3, 1.0, 1.2, 1.4, 1.6, 1.8]

# 散布図のプロット
plt.figure(figsize=(10, 8))
plt.scatter(release_year, cutting_edge_score)

# 色分け
experienced = ['HTML/CSS', 'Sass']
colors = ['red' if tech in experienced else 'blue' for tech in technologies]

# プロットとラベル追加
for i, tech in enumerate(technologies):
    plt.scatter(release_year[i], cutting_edge_score[i], color=colors[i])
    plt.text(release_year[i], cutting_edge_score[i], tech, fontsize=9)

# グラフのラベル
plt.xlabel('Release Year')
plt.ylabel('Cutting Edge Score (1-10)')
plt.title('Cutting Edge Score vs. Release Year of Technologies')

# 凡例の追加
red_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Experienced')
blue_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Unexperienced')
plt.legend(handles=[red_patch, blue_patch])

plt.grid(True)
plt.savefig('scatter_plot.png')
plt.show()

