#coding_for_advanced_week1

def read_references(file_path):
    references_dict = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
        for line in lines:
            if line[0].isdigit():
                ref_num = line.split('.')[0]
                ref_text = '.'.join(line.split('.')[1:]).replace(" ", "")
                references_dict[ref_num] = ref_text
    return references_dict

def compare_references(refs_dict_1, refs_dict_2):
    comparison_status = {}
    for idx in range(1, 61):
        ref_key = str(idx)
        ref1, ref2 = refs_dict_1.get(ref_key, ""), refs_dict_2.get(ref_key, "")
        if ref1 == ref2:
            comparison_status[ref_key] = ["GOOD"]
        else:
            diffs = []
            buffer = ""
            for char1, char2 in zip(ref1, ref2):
                if char1 != char2:
                    buffer += char1
                elif buffer:
                    diffs.append(buffer)
                    buffer = ""
            if buffer:
                diffs.append(buffer)
            if len(ref1) > len(ref2):
                diffs.append(ref1[len(ref2):])
            elif len(ref2) > len(ref1):
                diffs.append(ref1[len(ref1):])
            comparison_status[ref_key] = diffs if diffs else ["DIFF"]
    return comparison_status

def write_status(status_dict, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for key in sorted(status_dict, key=lambda x: int(x)):
            f.write(f"{key} : {', '.join(status_dict[key])}\n")

if __name__ == "__main__":
    refs_file_1 = read_references("references_1.txt")
    refs_file_2 = read_references("references_2.txt")
    ref_status = compare_references(refs_file_1, refs_file_2)
    write_status(ref_status, "ex_1_advanced_submit.txt")

