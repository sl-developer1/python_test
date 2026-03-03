def sort(width, height, length, mass):
    volume = width * height * length
    
    # Determine conditions
    bulky = volume >= 1000000 or max(width, height, length) >= 150
    heavy = mass >= 20
    
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


def main():
  width = 100
  height = 100
  length = 100
  mass = 10

  sort_condition_result = sort(width,height,length,mass)

  print(sort_condition_result)

if __name__ == "__main__":
    main()
