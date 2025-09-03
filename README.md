# 📘 Calculator Project  

A personal practice project in Python to strengthen knowledge of data structures (stacks) and parsing of mathematical expressions.  

---

## ✅ Progress so far  

- Implemented a **custom stack (MinimumStack)** using linked nodes.  
- Support for the **four basic operations**: addition, subtraction, multiplication, and division.  
- Handling of **negative numbers** in most cases.  
- Initial support for **decimal numbers**.  
- Better code organization through helper functions (`getNextNumber`, `Resolve`, etc.).  
- Immediate resolution of multiplication and division before storing results in the add/subtract stack.  

---

## 🐞 Known Bugs / Pending Improvements  

### 1. Negative numbers in multiplication/division  


Problematic example:  


Currently, the parser pushes `3.5` into the stack before applying the multiplication.  
This causes inconsistencies because the number should be treated as part of the ongoing operation.  

- **Current workaround**: perform a `pop` if no valid number exists.  
- **Ideal solution**: delay pushing numbers until the next operation is confirmed (*delayed push strategy*).  

---

### 2. Expression tokenization (pending)  
At the moment, the expression is processed character by character, which makes it harder to handle negatives and complex cases.  

- **Goal**: convert the string into a list of tokens, for example:

- [ ] **Fix negative number bug** in multiplication/division.  
- [ ] **Implement tokenization** of the input string before evaluation.  
- [ ] Improve handling of **decimal numbers** across all operations.  
