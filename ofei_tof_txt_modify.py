input_txt_file = '/home/brent/brentj/datasets/ofei_tof/point_cloud.txt'
output_txt_file = '/home/brent/brentj/datasets/ofei_tof/point_cloud_modified.txt'

f = open(input_txt_file, 'r')
ff = open(output_txt_file, 'w')
line = f.readline()
line = line.strip('}],"idx":1}]')
line = line[10:]
points = line.split('},{')
wt_lists = []
for point in points:
    p = point.split(':')
    x = int(p[1][:-4])
    y = int(p[2][:-4])
    z = int(p[3])
    wt_lists.append(x, y, z, '\n')

print(wt_lists)