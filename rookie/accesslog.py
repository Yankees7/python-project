import re


def count_patt(log_file, patt):
    patt_dict = {}
    with open(log_file) as fobj:
        for line in fobj:
            m = re.search(patt, line)
            if m:  # 如果m是None为假，非None为真
                k = m.group()
                patt_dict[k] = patt_dict.get(k, 0) + 1
    return patt_dict


if __name__ == '__main__':
    log_file = 'access_log'
    ip = "^(\d+\.){3}\d+"
    br = ''
    result1 = count_patt(log_file, ip)
    result2 = count_patt(log_file, br)
    print(result1)
