from members.hello_truong import truong_greeting
from members.hello_kiet import hello_kiet as kiet_greeting
from members.hello_huy import hello_huy as huy_greeting
from members.hello_phi import hello_phi as phi_greeting
from members.hello_tri import print_name as tri_greeting

def main():
    print("Hello, Day la loi chao tu cac thanh vien Group 2:")
    truong_greeting()
    kiet_greeting()
    huy_greeting()
    phi_greeting()
    tri_greeting()

if __name__ == '__main__':
    main()