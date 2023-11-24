import ipaddress
import argparse
import os

rules_path = os.path.join(os.path.dirname(__file__), 'rules.txt')

class Firewall:
    """Firewall class to manage addign and removing rules and listing rules based on rule number, direction, and address."""
    def __init__(self):
        self.rules = []

    def add_rule(self, rule_num, direction, addr):
        rule = {'rule_num': rule_num, 'direction': direction, 'addr': addr}
        self.rules.append(rule)
        self.rules.sort(key=lambda x: x['rule_num'])
        self.save_rules() # saving rules to file to retain rules after application restart

    def save_rules(self):
        with open(rules_path, 'a') as f:
            for rule in self.rules:
                f.write(f"{rule['rule_num']},{rule['direction']},{rule['addr']}\n")

    def remove_rule(self, rule_num, direction=None):
        self.rules = [r for r in self.rules if not (r['rule_num'] == rule_num and (direction is None or r['direction'] == direction))]

    def list_rules(self, rule_num=None, direction=None, addr=None):
        with open(rules_path, 'r') as f:
            filtered_rules = [{'rule_num': int(r[0]), 'direction': r[1], 'addr': r[2]} for r in [line.strip().split(',') for line in f.readlines()]]

        if rule_num is not None:
            filtered_rules = [r for r in filtered_rules if r['rule_num'] == rule_num]

        if direction is not None:
            filtered_rules = [r for r in filtered_rules if r['direction'] == direction]

        if addr is not None:
            addr = ipaddress.IPv4Network(addr, strict=False)
            filtered_rules = [r for r in filtered_rules if ipaddress.IPv4Address(r['addr']) in addr]

        return filtered_rules

def main():
    firewall = Firewall()

    parser = argparse.ArgumentParser(description='Firewall Rules Application')
    parser.add_argument('action', choices=['add', 'remove', 'list'], help='Action to perform')
    parser.add_argument('rule_num', type=int, nargs='?', default=1, help='Rule number')
    parser.add_argument('--in', action='store_const', const='in', dest='direction', help='Incoming traffic')
    parser.add_argument('--out', action='store_const', const='out', dest='direction', help='Outgoing traffic')
    parser.add_argument('addr', nargs='?', help='IPv4 address or address range')

    args = parser.parse_args()

    if args.action == 'add':
        if args.addr is None:
            print('Error: Address is required for "add" action.')
        else:
            firewall.add_rule(args.rule_num, args.direction, args.addr)
            print('Rule added successfully.')

    elif args.action == 'remove':
        firewall.remove_rule(args.rule_num, args.direction)
        print('Rule removed successfully.')

    elif args.action == 'list':
        rules = firewall.list_rules(args.rule_num, args.direction, args.addr)
        for rule in rules:
            print(f"Rule {rule['rule_num']}: {rule['direction']} - {rule['addr']}")

if __name__ == "__main__":
    main()
    main()
    if_name
