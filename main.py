from members.hello_truong import print_name as truong_greeting
from members.hello_kiet import hello_kiet as kiet_greeting
def main():
    print("Hello, Day la loi chao tu cac thanh vien:")
    truong_greeting()
    kiet_greeting()



if __name__ == '__main__':
    main()