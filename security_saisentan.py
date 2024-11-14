import matplotlib.pyplot as plt

# データの準備
technologies = ['TLS/SSL', 'AES', 'OAuth', 'SAML', 'OpenID Connect', 'Zero Trust Security', 'Kerberos', 'PKI', 'RADIUS', 'Multi-factor Authentication (MFA)']
release_year = [1995, 2001, 2010, 2002, 2014, 2010, 1983, 1976, 1991, 2003]
cutting_edge_score = [9.0, 9.5, 9.2, 8.8, 9.0, 9.1, 8.0, 7.5, 7.8, 8.5]

# 散布図のプロット
plt.figure(figsize=(10, 8))

# 色分け
colors = ['blue' for _ in technologies]

# プロットとラベル追加
for i, tech in enumerate(technologies):
    plt.scatter(release_year[i], cutting_edge_score[i], color=colors[i])
    plt.text(release_year[i], cutting_edge_score[i], tech, fontsize=9)

# グラフのラベル
plt.xlabel('Release Year')
plt.ylabel('Cutting Edge Score (1-10)')
plt.title('Cutting Edge Score vs. Release Year of Security Technologies')
plt.ylim(1, 10)  # Y軸の範囲を1～10に設定

# 凡例の追加
blue_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Security Technologies')
plt.legend(handles=[blue_patch])

plt.grid(True)
plt.savefig('security_scatter_plot.png')
plt.show()

