
# Python Quick Codes
Mixed quick codes

> Codes will be categorized as they increase 🤔

### Operations On A Global Variable
<details>
<summary>A Code With Error</summary>

```python
counter = 0
def increase():
   counter += 1

increase()
print(counter)
```
Error:

```
Traceback (most recent call last):
  File "temp.py", line 8, in <module>
    increase()
  File "temp.py", line 5, in increase
    counter+=1
UnboundLocalError: local variable 'counter' referenced before assignment
```
</details>


<details>


<summary>Error-free Code</summary>

```python
counter = 0
def increase():
   global counter
   counter += 1

increase()
print(counter)

# Output: 1
```

</details>
