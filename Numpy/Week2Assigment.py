import numpy as np

Sale_Amount,Serial_Number,List_Year,Town,Assessed_Value = np.genfromtxt('Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter =',', usecols=(6,0,1,3,5), unpack = True, dtype = None, skip_header = 1,invalid_raise=False)

print (Sale_Amount)
print (Serial_Number)
print (List_Year)
print (Town)
print (Assessed_Value)



print("Sale Amount:\n", Sale_Amount)
print("Serial Number:\n", Serial_Number)
print("List Year:\n", List_Year)
print("Town:\n", Town)
print("Assessed Value:\n", Assessed_Value)

print("----------------------")
#2
md = np.mean(Sale_Amount)
v = np.std(Sale_Amount)
print("Mode of Sale_Amount: " , md)
print("standard of Sale_Amount:" , v)

print("-----------------")
#3 
md_a = np.mean(Assessed_Value)
v_a = np.std(Assessed_Value)
print("Mode of Sale_Amount: " , md_a)
print("standard of Sale_Amount:" , v_a)


print("--------------------")
#4 
Addition = Sale_Amount + Assessed_Value
Substrat = Sale_Amount - Assessed_Value
Multiply = Sale_Amount * Assessed_Value


Add = np.add(Sale_Amount, Assessed_Value)
Sub = np.subtract(Sale_Amount, Assessed_Value)
Mul = np.multiply(Sale_Amount, Assessed_Value)


print ("Addition By Opration +:" ,Addition)
print ("Substrat By Opration -:" , Substrat)
print ("Multiple By Opration *:" , Multiply)

print ("By method add" , Add)
print ("By method sub" , Sub)
print ("By method mul" , Mul)


print ("------------------------------------------")

#5:  2 dimentional arrary

new_2D_array = np.array ([Sale_Amount , Assessed_Value])

print ("2D array :" , new_2D_array )


print ("-------------------------")

#6: 3 imentional arrary

new_3D_array = np.array ([Sale_Amount , Assessed_Value , List_Year])

print ("3D array :" , new_3D_array)


print ("-------------------------")

# 7 
for e in np.nditer(Sale_Amount):
    print(e)

#8 
for index, e in np.ndenumerate(Sale_Amount):
        print(index , e)


print ("-------------------------")
#9 
sale_amount_array = np.array(Sale_Amount)

# 7 common properties of the Sale_Amount array

print("Number of dimensions (ndim):", sale_amount_array.ndim)
print("Shape of the array (shape):", sale_amount_array.shape)
print("Total number of elements (size):", sale_amount_array.size)
print("Data type of the elements (dtype):", sale_amount_array.dtype)
print("Memory address of the data buffer (data):", sale_amount_array.data)
print("Number of bytes per element (itemsize):", sale_amount_array.itemsize)
print("Total bytes consumed by the elements (nbytes):", sale_amount_array.nbytes)


print ("-------------------------")
#10

# 2D array by slice 'Sale Amount' and 'Assessed Value'
two_d_array = np.column_stack((Sale_Amount, Assessed_Value))

# row and column indices for slicing
start_row = 2  
end_row = 7    
start_col = 1  
end_col = 4    


sliced_array = two_d_array[start_row:end_row, start_col:end_col]

print("Original 2D Array (rows 0-9):")
print(two_d_array[:10])
print("\nSliced Array (rows 3rd to 7th, columns 2nd to 4th):")
print(sliced_array)


print ("====================")

#11
data_2D = np.column_stack((Sale_Amount, Serial_Number, List_Year, Town, Assessed_Value))
sliced_data = data_2D[1:8, 2:5]

print(sliced_data)

print ("====================")
#12

# 2D array using the assessed values
assessed_values_2D = np.column_stack((Assessed_Value, Assessed_Value))

# Apply geometric operations
sin_values = np.sin(assessed_values_2D)
cos_values = np.cos(assessed_values_2D)

print("Sin values:\n", sin_values)
print("Cos values:\n", cos_values)

print ("====================")
