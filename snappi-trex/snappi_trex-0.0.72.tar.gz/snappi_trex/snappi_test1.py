import sys, os

trex_path = '/opt/trex/v2.89/automation/trex_control_plane/interactive'
sys.path.insert(0, os.path.abspath(trex_path))

import snappi
import trexapi as snappi_trex



def hello_snappi():
    """
    This script does following:
    - Send 1000 packets back and forth between the two ports at a rate of
      1000 packets per second.
    - Validate that total packets sent and received on both interfaces is as
      expected using port metrics.
    - Validate that captured UDP packets on both the ports are as expected.
    """
    # create a new API instance where host points to controller
    api = snappi_trex.trexapi.Api()
    
    # and an empty traffic configuration to be pushed to controller later on
    cfg = api.config()

    # add two ports where location points to traffic-engine (aka ports)
    p1, p2 = (
        cfg.ports
        .port(name='p1', location='localhost:5555')
        .port(name='p2', location='localhost:5556')
    )

    # add layer 1 property to configure same speed on both ports
    ly = cfg.layer1.layer1(name='ly')[-1]
    ly.port_names = [p1.name, p2.name]
    ly.speed = ly.SPEED_1_GBPS

    # enable packet capture on both ports
    cp = cfg.captures.capture(name='cp')[-1]
    cp.port_names = [p1.name, p2.name]

    # add two traffic flows
    f1, f2 = cfg.flows.flow(name='flow p1->p2').flow(name='flow p2->p1')
    # and assign source and destination ports for each
    f1.tx_rx.port.tx_name, f1.tx_rx.port.rx_name = p1.name, p2.name
    f2.tx_rx.port.tx_name, f2.tx_rx.port.rx_name = p2.name, p1.name

    # configure packet size, rate and duration for both flows
    f1.size.fixed = 128
    f2.size.fixed = 256
    # f1.size.increment.start = f2.size.random.min = 128
    # f1.size.increment.end = f2.size.random.max = 256
    # f1.size.increment.step = 2
    for f in cfg.flows:
        # send 1000 packets and stop
        f.duration.fixed_packets.packets = 1000
        # send 1000 packets per second
        f.rate.pps = 1000

    # configure packet with Ethernet, IPv4 and UDP headers for both flows
    eth1, ip1, ip12, udp1, udp12 = f1.packet.ethernet().ipv4().ipv4().udp().udp()
    eth2, ip2, ip22, udp2, udp22 = f2.packet.ethernet().ipv4().ipv4().udp().udp()

    # set source and destination MAC addresses
    # eth1.src.value, eth1.dst.value = '00:AA:00:00:04:00', '00:AA:00:00:00:AA'
    eth2.src.value, eth2.dst.value = '00:AA:00:00:00:AA', '00:AA:00:00:04:00'
    eth1.src.increment.start = '10:AA:00:00:04:00'
    eth1.src.increment.step = 2
    eth1.src.increment.count = 1000
    eth2.src.values = ['33:33:33:11:11:11', '22:22:22:22:22:22']
    eth1.dst.decrement.start = '10:AA:00:00:04:00'
    eth1.dst.decrement.step = 4
    eth1.dst.decrement.count = 1000

    # set source and destination IPv4 addresses
    # ip1.src.value, ip1.dst.value = '10.0.0.1', '10.0.0.2'
    ip2.src.value, ip2.dst.value = '10.0.0.2', '10.0.0.1'
    ip22.src.value, ip22.dst.value = '10.0.0.3', '10.0.0.4'
    ip12.src.value, ip12.dst.value = '10.0.0.1', '10.0.0.2'

    ip1.src.increment.start = '11.0.0.1'
    ip1.src.increment.step = 2
    ip1.src.increment.count = 1000
    ip1.dst.decrement.start = '12.0.0.0'
    ip1.dst.decrement.step = 4
    ip1.dst.decrement.count = 1000

    # set incrementing port numbers as source UDP ports
    udp12.src_port.value = 5001
    udp22.src_port.value = 5002
    udp1.src_port.value = 5000
    # udp2.src_port.value = 5003
    # udp1.src_port.increment.start = 5000
    # udp1.src_port.increment.step = 1
    # udp1.src_port.increment.count = 1000
    udp2.src_port.decrement.start = 5000
    udp2.src_port.decrement.step = 1
    udp2.src_port.decrement.count = 1000

    # assign list of port numbers as destination UDP ports
    udp12.dst_port.value = 5001
    udp22.dst_port.value = 5002
    # udp1.dst_port.value = 5000
    # udp2.dst_port.value = 5003
    # udp1.dst_port.increment.start = 5000
    # udp1.dst_port.increment.step = 1
    # udp1.dst_port.increment.count = 1000
    udp2.dst_port.decrement.start = 5000
    udp2.dst_port.decrement.step = 1
    udp2.dst_port.decrement.count = 1000
    udp1.dst_port.values = [8000, 8004, 8049, 9001]

    print(cfg.serialize())

    

    print('Pushing traffic configuration ...')
    api.set_config(cfg)

    # print('Starting packet capture on all configured ports ...')
    # cs = api.capture_state()
    # cs.state = cs.START
    # api.set_capture_state(cs)

    print('Starting transmit on all configured flows ...')
    ts = api.transmit_state()
    ts.state = ts.START
    api.set_transmit_state(ts)

    # print('Checking metrics on all configured ports ...')
    # print('Expected\tTotal Tx\tTotal Rx')
    # assert wait_for(lambda: metrics_ok(api, cfg)), 'Metrics validation failed!'

    # assert captures_ok(api, cfg), 'Capture validation failed!'

    # print('Test passed !')


def metrics_ok(api, cfg):
    # create a port metrics request and filter based on port names
    req = api.metrics_request()
    req.port.port_names = [p.name for p in cfg.ports]
    # include only sent and received packet counts
    req.port.column_names = [req.port.FRAMES_TX, req.port.FRAMES_RX]

    # fetch port metrics
    res = api.get_metrics(req)
    # calculate total frames sent and received across all configured ports
    total_tx = sum([m.frames_tx for m in res.port_metrics])
    total_rx = sum([m.frames_rx for m in res.port_metrics])
    expected = sum([f.duration.fixed_packets.packets for f in cfg.flows])

    print('%d\t\t%d\t\t%d' % (expected, total_tx, total_rx))

    return expected == total_tx and total_rx >= expected


def captures_ok(api, cfg):
    import dpkt
    print('Checking captured packets on all configured ports ...')
    print('Port Name\tExpected\tUDP packets')

    result = []
    for p in cfg.ports:
        exp, act = 1000, 0
        # create capture request and filter based on port name
        req = api.capture_request()
        req.port_name = p.name
        # fetch captured pcap bytes and feed it to pcap parser dpkt
        pcap = dpkt.pcap.Reader(api.get_capture(req))
        for _, buf in pcap:
            # check if current packet is a valid UDP packet
            eth = dpkt.ethernet.Ethernet(buf)
            if isinstance(eth.data.data, dpkt.udp.UDP):
                act += 1

        print('%s\t\t%d\t\t%d' % (p.name, exp, act))
        result.append(exp == act)

    return all(result)


def wait_for(func, timeout=10, interval=0.2):
    """
    Keeps calling the `func` until it returns true or `timeout` occurs
    every `interval` seconds.
    """
    import time
    start = time.time()

    while time.time() - start <= timeout:
        if func():
            return True
        time.sleep(interval)

    print('Timeout occurred !')
    return False


if __name__ == '__main__':
    hello_snappi()
