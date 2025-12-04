import scipy.stats as stats

# 准备您的两组配对数据
list_A = [96.3, 96.2, 96.3, 96.4, 96.5, 96.4]  # Baseline的结果
list_B = [96.4, 96.7, 97.0, 96.6, 96.4, 96.5]  # + C-GKAN的结果

# 执行威尔科克森符号秩检验
# alternative='less' 表示我们检验 A 是否显著小于 B
# 这等价于检验 B 是否显著大于 A
statistic, p_value = stats.wilcoxon(list_A, list_B, alternative='less')

print(f"P-value: {p_value}")

# 判断是否显著
if p_value < 0.05:
    print("提升是统计显著的 (Reject H₀)")
else:
    print("提升不具有统计显著性 (Fail to reject H₀)")