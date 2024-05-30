import numpy as np 



#arr = np.array  ([1,2,3,4,5])

#print(arr)
#print(type(arr))


#arr = np.zeros((3, 4))
#print(arr)


#rr = np.ones((3, 4))
#print(arr)



#arr = np.ones((3, 4)) * 5
#print(arr)


#arr = np.arange(10, 100, 10)
#print(arr)


#arr = np.arange(12)
#print(arr)



#arr = np.arange(12).reshape(3, 4)
#print(arr)



#arr = np.arange(12).reshape(4, 3)
#print(arr)


# ndim  ->  Boyut sayısını verir
# shape ->  Dizi boyutunu verir
# size  ->  Dizideki eleman sayısını verir
# dtype ->  Dizideki eleman sayısını döndürür

arr2d = np.arange(12).reshape(4, 3)
arr3d = np.array([[[1, 2], [3 ,4], [5,6], [7,8]]])
#print(arr2d.ndim)
#print(arr3d.ndim)
#print(arr2d.shape)
#print(arr3d.shape)
#print(arr2d.size)
#print(arr3d.size)
#print(arr2d.dtype)
#print(arr3d.dtype)


#arr = np.array([1,2,3,4,5])
#arr = np.array([1,2,3,4,5], np.int8)
#arr = np.array([1,2,3,4,5], np.uint16)
print(arr.dtype)