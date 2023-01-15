import streamlit as st
st.header("TRUTH TABLE FOR LOGICAL GATES")
Operation = st.text_input('Enter Operation to be performed AND, OR, NAND, XOR, NOT, NOR and XNOR')
st.write("Resultant Table : ", Operation)
a = 0
b = 0

 
if Operation == 'AND':
    data = [
        ["A", "B", "A AND B"],
        [a, a, a and a],
        [a, b, a and b],
        [b, a, b and a],
        [b, b, b and b],
    ]
    
    st. table(data)
elif Operation == 'OR':
    data = [
        ["A", "B", "A OR B"],
        [a, a, a or a],
        [a, b, a or b],
        [b, a, b or a],
        [b, b, b or b],
    ]
    
    st. table(data)

elif Operation == 'NOT':
    
    data = [        
        [a, not a],
        [not a, a]        
    ]

    st. table(data)

elif Operation == 'NAND':
    
    data = [
        ["A", "B", "A NAND B"],
        [a, a, not (a and a)],
        [a, b, not (a and b)],
        [b, a, not (b and a)],
        [b, b, not (b and b)],
    ]

    st. table(data)

elif Operation == 'NOR':
    
    data = [
        ["A", "B", "A NOR B"],
        [a, a, not (a or a)],
        [a, b, not (a or b)],
        [b, a, not (b or a)],
        [b, b, not (b or b)],
    ]

    st. table(data)

elif Operation == 'XOR':
    data = [
        ["A", "B", "A XOR B"],
        [a, a, a ^ a],
        [a, b, a ^ b],
        [b, a, b ^ a],
        [b, b, b ^ b],
    ]

    st. table(data)

elif Operation == 'XNOR':
    data = [
        ["A", "B", "A XNOR B"],
        [a, a, not (a ^ a)],
        [a, b, not (a ^ b)],
        [b, a, not (b ^ a)],
        [b, b, not (b ^ b)],
    ]

    st. table(data)

