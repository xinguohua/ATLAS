def load_malicious_labels(label_file):
    """读取恶意节点标签，返回一个集合"""
    with open(label_file, 'r') as f:
        return set(line.strip() for line in f if line.strip())

def filter_txt_file_by_labels(input_file, malicious_nodes, output_file):
    """过滤txt文件，仅保留包含恶意节点的行"""
    with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
        for line in fin:
            if any(node in line for node in malicious_nodes):
                fout.write(line)

if __name__ == "__main__":
    # 文件路径（请根据实际情况修改）
    label_file = "/home/nsas2020/fuzz/ATLAS/process/raw_logs/M1-CVE-2015-5122_windows_h1/malicious_labels.txt"
    input_txt_file = "/home/nsas2020/fuzz/ATLAS/process/seq/seq_graph_M1-CVE-2015-5122_windows_h1.dot.txt"
    output_txt_file = "filtered_graph.txt"

    malicious_nodes = load_malicious_labels(label_file)
    filter_txt_file_by_labels(input_txt_file, malicious_nodes, output_txt_file)

    print(f"Filtered file saved to: {output_txt_file}")