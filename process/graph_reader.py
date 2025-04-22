from networkx.drawing.nx_pydot import read_dot
import os
import time


if __name__ == '__main__':
    for file in os.listdir("graph"):
        start = time.time()
        written_lines = []
        print("\n============\nprocessing the graph: " + file)
        G = read_dot("graph/" + file)
        output_file_path = "seq/" + "seq_" + file + ".txt"
        if os.path.exists(output_file_path):
          os.remove(output_file_path)

        output_file = open(output_file_path, "a")

        for a, b, data in sorted(G.edges(data=True), key=lambda x: x[2]['timestamp']):
            op_type = data['type']
            #  or op_type == "connect" op_type == "read" or op_type == "executed"
            if op_type == "bind" or op_type == "sock_send" or op_type == "connect" or op_type == "write" or op_type == "delete" or op_type == "fork" or op_type == "resolve" or op_type == "web_request" or op_type == "refer":
                formatted_str = '{b} {w} {a}\n'.format(a=a.lstrip().rstrip().replace(" ", ""), w=op_type, b=b.lstrip().rstrip().replace(" ", ""))
                if not formatted_str in written_lines:
                    output_file.write(formatted_str)
                    written_lines.append(formatted_str)
            else:
                formatted_str = '{a} {w} {b}\n'.format(a=a.lstrip().rstrip().replace(" ", ""), w=op_type, b=b.lstrip().rstrip().replace(" ", ""))
                if not formatted_str in written_lines:
                    output_file.write(formatted_str)
                    written_lines.append(formatted_str)

        done = time.time()
        elapsed = done - start
        print("processing time: " + str(elapsed))

        print("The graph has been turned into sequence of events, output saved to " + output_file_path)
