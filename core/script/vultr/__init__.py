import os
import requests

from pyquery import PyQuery

from core.util import ping

NODE_LINE_SPLIT = '='
NODE_FILE_PATH = os.path.join(os.path.abspath(os.curdir), 'vultr_node.txt')


def ping_node():
    print('----- Vultr node ping test start. -----')
    result = ''
    with open(NODE_FILE_PATH, 'r') as f:
        for node in f:
            name, url = node.replace('\n', '').split(NODE_LINE_SPLIT)
            print('----- Ping ({}) node start. -----'.format(name))
            content = ping(url, 10).split('\n')

            ttl_sum = 0.0
            time_sum = 0.0
            for line in content:
                split_result = line.split(' ')
                if line.find('icmp_seq') > 0 and line.find('timeout') == -1:
                    ttl_sum += float(split_result[5].split('=')[1])
                    time_sum += float(split_result[6].split('=')[1])

            statistics = content[-3].split(', ')
            transmitted = statistics[0].split(' ')[0]
            received = statistics[1].split(' ')[0]
            loss = statistics[2].split(' ')[0]

            result += '{name}: {statistics}, ttl_avg {ttl}.2f, time_avg {time}\n'.format(
                name=name,
                statistics=statistics,
                ttl=round(ttl_sum / float(received), 2),
                time=round(time_sum / float(received), 2)
            )
            print('----- Ping ({}) node end. -----'.format(name))
    print('----- Vultr node ping test end. -----')
    print(result)


def update_node():
    vultr_node_url = 'https://www.vultr.com/faq/#downloadspeedtests'

    with requests.get(vultr_node_url) as resp:
        root_node = PyQuery(PyQuery(resp.text)('#speedtest_v4'))
        tr_node_list = PyQuery(PyQuery(root_node)('td'))

        assert len(tr_node_list) % 3 == 0

        with open(NODE_FILE_PATH, 'w') as f:
            for i in range(len(tr_node_list) // 3):
                name = PyQuery(tr_node_list[i * 3]).text()
                url = PyQuery(tr_node_list[i * 3 + 1]).text()
                f.write('{}{}{}\n'.format(name, NODE_LINE_SPLIT, url))


if __name__ == '__main__':
    ping_node()
