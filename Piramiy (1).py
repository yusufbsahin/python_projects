while True:
    user_input = input("Gir abijim bi rakam: (q ile çıkarsın): ")

    if user_input.lower() == 'q':
        print("hadi selametle👋")
        break

    try:
        n = int(user_input)

        
        print("\n".join((i*"🔲").center(n*2) for i in range(1, n*2, 2)))
    except ValueError:
        print("olmaz abi rakam giricen, bizi mi yiyosun")
