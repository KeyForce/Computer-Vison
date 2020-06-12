def cal_iou(box1, box2):

    xmin1, ymin1, xmax1, ymax1 = box1
    xmin2, ymin2, xmax2, ymax2 = box2
    
    s1 = (xmax1 - xmin1) * (ymax1 - ymin1)
    s2 = (xmax2 - xmin2) * (ymax2 - ymin2)
 
    
    xmin = max(xmin1, xmin2)
    ymin = max(ymin1, ymin2)
    xmax = min(xmax1, xmax2)
    ymax = min(ymax1, ymax2)
 
    w = max(0, xmax - xmin)
    h = max(0, ymax - ymin)
    area = w * h  
    iou = area / (s1 + s2 - area+1e-6)
    return iou

bbox = []
w, h, s, t, k, p, q = map(int,input().split())
for i in range(k):
    obj_x, obj_y, obj_w, obj_h = map(int,input().split())
    obj_xx, obj_yy = obj_w + obj_x, obj_h + obj_y
    if 0<=obj_x<=p-1 and 0<=obj_y<=q-1 and 1<=obj_w<=500 and 1<=obj_h<=500:
        bbox.append([obj_x, obj_y, obj_xx, obj_yy])


anchor_bbox =[]
for i in range(p):
    for j in range(q):
        if s*i+w<=p and t*j+h<=q:
            anchor_bbox.append([s*i, t*j, s*i+w, t*j+h])


if k<10:
    res = 0
    for j in bbox:
        for i in anchor_bbox:
            iou = cal_iou(j, i)
            if iou > 0.0:
                res = res + 1
    print(res)
else:
    out_x = min([x[0] for x in bbox])
    out_y = min([x[1] for x in bbox])
    out_xx = max([x[2] for x in bbox])
    out_yy = max([x[3] for x in bbox])

    if out_xx > p:
        out_xx = p
    if out_yy > q:
        out_yy = q

    max_bbox = [out_x, out_y, out_xx, out_yy]
    res = 0
    for i in anchor_bbox:
        iou = cal_iou(max_bbox, i)
        if iou > 0.0:
            res = res + 1

    print(res)