import os
from shutil import copyfile
import glob
import re


class EnvManage:
    def __init__(self, img_file_path, target_file_path, img_dis_path_dir, target_dis_path_dir):
        self.img_file_path = img_file_path
        self.target_file_path = target_file_path
        self.img_dis_path_dir = img_dis_path_dir
        self.target_dis_path_dir = target_dis_path_dir

    def windows_dispose(self):
        image_file_sort = sorted(glob.glob(self.img_file_path))
        target_file_sort = sorted(glob.glob(self.target_file_path))
        image_file_re = re_widows(image_file_sort, self.img_dis_path_dir, ".jpg")
        target_file_re = re_widows(target_file_sort, self.target_dis_path_dir, '.txt')
        print(image_file_re)
        file_mkdir(self.img_dis_path_dir)
        for i, j in zip(image_file_sort, image_file_re):
            if os.path.exists(j):
                print("{}文件已存在".format(j))
            else:
                copyfile(i, j)
        file_mkdir(self.target_dis_path_dir)
        for i, j in zip(target_file_sort, target_file_re):
            if os.path.exists(j):
                print("{}文件已存在".format(j))
            else:
                copyfile(i, j)

    def linux_dispose(self):
        image_file_sort = sorted(glob.glob(self.img_file_path))
        target_file_sort = sorted(glob.glob(self.target_file_path))
        image_file_re = re_linux(image_file_sort, self.img_dis_path_dir, ".jpg")
        target_file_re = re_linux(target_file_sort, self.target_dis_path_dir, '.txt')
        print(image_file_re)
        file_mkdir(self.img_dis_path_dir)
        for i, j in zip(image_file_sort, image_file_re):
            if os.path.exists(j):
                print("{}文件已存在".format(j))
            else:
                copyfile(i, j)
        file_mkdir(self.target_dis_path_dir)
        for i, j in zip(target_file_sort, target_file_re):
            if os.path.exists(j):
                print("{}文件已存在".format(j))
            else:
                copyfile(i, j)


def re_widows(file_name_list, path_dir, suffix):
    file_name_list_re = []
    for file_name in file_name_list:
        file_name_list_re.append(
            path_dir + "\\" + "%05d" % (int(re.findall(r"\\(\d+)%s" % suffix, file_name)[0])) + suffix)
    return file_name_list_re


def re_linux(file_name_list, path_dir, suffix):
    file_name_list_re = []
    for file_name in file_name_list:
        file_name_list_re.append(
            path_dir + "/" + "%05d" % (int(re.findall(r"/(\d+)%s" % suffix, file_name)[0])) + suffix)
    return file_name_list_re


def file_mkdir(file_path):
    if os.path.exists(file_path):
        print("{}文件夹已存在".format(file_path))
    else:
        os.mkdir(file_path)
        print("{}创建成功".format(file_path))


if __name__ == '__main__':
    # 源地址
    img_file_path = r"G:\光谷公司\ctw1500\test\text_image\\*.jpg"
    target_file_path = r"G:\光谷公司\ctw1500\test\text_label_circum\\*.txt"
    # 保存目的地址
    img_dis_path_dir = r"G:\光谷公司\ctw1500\image"
    target_dis_path_dir = r"G:\光谷公司\ctw1500\Annos"
    aa = EnvManage(img_file_path, target_file_path, img_dis_path_dir, target_dis_path_dir)
    aa.windows_dispose()
    # aa.linux_dispose()
