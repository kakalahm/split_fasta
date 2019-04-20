import re
import math
if __name__ == "__main__":
    num_files = 2
    data_fp = "All_Unigene_MSHit.fa"
    
    with open(data_fp, "r") as f:
        raw_txt = f.read()
    splits = re.split(r"^>", raw_txt, flags=re.MULTILINE)[1:]

    # num_lines = len(splits) // num_files
    num_lines = math.ceil(len(splits) / num_files)
    all_lists = []
    new_list = []
    for ii, item in enumerate(splits):
        new_list.append(">" + item)
        if ii % num_lines == num_lines - 1:  # new_list里的元素达到num_lines就把这个list保存起来，然后另开一个新的list
            all_lists.append(new_list)
            new_list = []
    # 把最后剩下的那个不够num_lines个元素的list也存起来

    if length(new_list)>0:
        all_lists.append(new_list)

  

    for ii, sub_list in enumerate(all_lists):
        with open("new_sub_file_{:03d}.fa".format(ii), "w") as f:
            f.write("".join(sub_list))
            #用.join函数将列表里的元素转成字符串并合并到一起
