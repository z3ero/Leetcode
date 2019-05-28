def ip_to_num(ip):
    ip_strs = [int(x) for x in ip.split('.')]
    return sum(ip_strs[i]<<[24,16,8,0][i] for i in range(4))

def num_to_ip(num):
    ip_strs = (str((num<<[24,16,8,0][i])%256) for i in range(4))
    return '.'.join(ip_strs)

if __name__=="__main__":
    ip = '127.0.0.1'
    num = ip_to_num(ip)
    print(num)
    new_ip = num_to_ip(num)
    print(ip)