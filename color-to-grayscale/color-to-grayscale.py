def color_to_grayscale(image):
    H = len(image)
    W = len(image[0])
    
    gray = []
    
    for i in range(H):
        row = []
        for j in range(W):
            R = image[i][j][0]
            G = image[i][j][1]
            B = image[i][j][2]
            
            Y = 0.299 * R + 0.587 * G + 0.114 * B
            row.append(Y)
        
        gray.append(row)
    
    return gray