def run():
    my_dictionary = {
          'key1': 1,
          'key2': 2,
          'key3': 3,
    }
    print(my_dictionary)
# {'key1': 1, 'key2': 2, 'key3': 3}
  
  
    print(my_dictionary['key1'])
    print(my_dictionary['key2'])
    print(my_dictionary['key3'])
# 1
# 2
# 3

    countries_population = {
        'Germany': 84396154,
        'France': 65602790,
        'Netherlands':17221305,
        'Belgium': 11705210
    }
    print(countries_population['France'])
    # 65602790


    # print(countries_population['Monaco'])
    # Traceback (most recent call last):
    # File "dictionary.py", line 33, in <module>
    #     run()
    # File "dictionary.py", line 28, in run
    #     print(countries_population['Monaco'])
    # KeyError: 'Monaco'

    for countries in countries_population.keys():
        print(countries)
    # Germany
    # France
    # Netherlands
    # Belgium

    for countries in countries_population.values():
        print(countries)
    # 84396154
    # 65602790
    # 17221305
    # 11705210

    for countries, population in countries_population.items():
        print(countries + ' have the current population of ' + str(population))


if __name__ == '__main__':
    run()