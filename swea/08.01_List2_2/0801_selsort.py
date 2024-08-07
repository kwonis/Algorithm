def selection_sort(arr,N): # arr 대상 ,N은 원소갯수
    for i in range(N-1):# 주어진 구간에 대해 ... 기준위치 i를 정하고
        min_idx =1
        for j in range(i+1, N ):
            if arr[min_idx]>arr[j]:
                min_idx =j
        arr[i], arr[min_idx]= arr[min_idx],arr[i]



A =[2,7,5,3,4]
B =[4,3,2,1]
selection_sort(A, len(A))
selection_sort(B, len(B))
print(A)