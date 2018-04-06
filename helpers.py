def dump_tc(tc):
    print ' '.join([format(x, '02X') for x in tc.build()])