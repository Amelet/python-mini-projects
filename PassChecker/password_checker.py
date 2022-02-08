import requests
import hashlib
import sys


def request_api_data(query_chr):
    url = "https://api.pwnedpasswords.com/range/" + query_chr
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching {res.status_code}")
    return res


def get_password_leaks_counts(hashes, hash_to_check):
    hashes = [line.split(":") for line in hashes.text.splitlines()]
    for hash, count in hashes:
        if hash == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # step1: UTF encode the password's string
    pass_utf8 = password.encode("utf-8")

    # step2: hash it into sha1 object
    pass_sha1_obj = hashlib.sha1(pass_utf8)

    # step3: hexdigest the object
    password_sha1 = pass_sha1_obj.hexdigest().upper()

    # step4: retrieve first five characters of your password
    first5_char, tail = password_sha1[:5], password_sha1[5:]
    print(first5_char)

    # step5: check the password's first5
    response = request_api_data(first5_char)
    result = get_password_leaks_counts(response, tail)
    return result


def main(args):
    for password in args:
        result = pwned_api_check(password)
        if result:
            print(f"password was found {result} times")
        else:
            print(f"password was NOT found")


if __name__ == "__main__":
    list_of_passwords = []
    with open("list_to_check.txt", "r") as file:
        for line in file:
            splittedline = line.split(sep=",")
            for i in range((len(splittedline))):
                list_of_passwords.append(splittedline[i])


    # list_of_passwords = sys.argv[1:] # pass the list at command line
    main(list_of_passwords)