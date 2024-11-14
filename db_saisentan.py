import matplotlib.pyplot as plt

# データの準備
technologies = ['MySQL', 'PostgreSQL', 'MongoDB', 'Redis', 'Cassandra', 'SQLite', 'Oracle Database', 'Microsoft SQL Server', 'MariaDB', 'CouchDB',
                'Ingres', 'dBase', 'Paradox', 'IBM DB2', 'Sybase', 'Firebird', 'HBase', 'Neo4j', 'Couchbase', 'Amazon DynamoDB', 
                'ArangoDB', 'OrientDB']
release_year = [1995, 1996, 2009, 2009, 2008, 2000, 1979, 1989, 2009, 2005,
                1980, 1979, 1985, 1983, 1984, 2000, 2007, 2007, 2011, 2012,
                2011, 2010]
cutting_edge_score = [9.0, 9.5, 9.2, 8.8, 8.0, 8.5, 7.0, 7.5, 8.2, 7.8,
                      3.0, 2.5, 3.2, 3.5, 4.0, 5.0, 6.0, 6.5, 7.0, 7.5,
                      5.8, 6.2]

# 散布図のプロット
plt.figure(figsize=(10, 8))

# 色分け
experienced = ['MySQL', 'PostgreSQL']
colors = ['red' if tech in experienced else 'blue' for tech in technologies]

# プロットとラベル追加
for i, tech in enumerate(technologies):
    plt.scatter(release_year[i], cutting_edge_score[i], color=colors[i])
    plt.text(release_year[i], cutting_edge_score[i], tech, fontsize=9)

# グラフのラベル
plt.xlabel('Release Year')
plt.ylabel('Cutting Edge Score (1-10)')
plt.title('Cutting Edge Score vs. Release Year of Database Technologies')
plt.ylim(1, 10)  # Y軸の範囲を1～10に設定

# 凡例の追加
red_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Experienced')
blue_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='UnExperienced')
plt.legend(handles=[red_patch, blue_patch])

plt.grid(True)
plt.savefig('db_scatter_plot.png')
plt.show()

