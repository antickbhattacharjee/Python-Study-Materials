a = 5   # 0101
b = 3   # 0011
print(a & b)   # 1
print(a | b)   # 7
print(a ^ b)   # 6
print(~a)      # -6 (inverts all bits and adds 1 in 2's complement)
print(a << 1)  # 10 (left shift = multiply by 2)
print(a >> 1)  # 2  (right shift = divide by 2)


'''
| Operator | Name        | Description                          |                            |
| -------- | ----------- | ------------------------------------ | -------------------------- |
| `&`      | AND         | Bits set in both operands            |                            |
| |`       | \`          | OR                                   | Bits set in either operand |
| `^`      | XOR         | Bits set in only one operand         |                            |
| `~`      | NOT         | Inverts all bits                     |                            |
| `<<`     | Left Shift  | Shifts bits left (multiplies by 2^n) |                            |
| `>>`     | Right Shift | Shifts bits right (divides by 2^n)   |                            |

| Decimal | Binary |
| ------- | ------ |
| 0       | 0000   |
| 1       | 0001   |
| 2       | 0010   |
| 3       | 0011   |
| 4       | 0100   |
| 5       | 0101   |
| 6       | 0110   |
| 7       | 0111   |
| 8       | 1000   |
| 9       | 1001   |

'''
