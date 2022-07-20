#Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 6.4 Module 6 Assignment

#Question 7

famous_list = '''\
Marilyn Monroe (1926 – 1962) American actress, singer, model
Abraham Lincoln (1809 – 1865) US President during American civil war
Nelson Mandela (1918 – 2013)  South African President anti-apartheid campaigner
John F. Kennedy (1917 – 1963) US President 1961 – 1963
Martin Luther King (1929 – 1968)  American civil rights campaigner
Queen Elizabeth II (1926 – ) British monarch since 1954
Winston Churchill (1874 – 1965) British Prime Minister during WWII
Donald Trump (1946 – ) Businessman, US President.
Bill Gates (1955 – ) American businessman, founder of Microsoft
Muhammad Ali (1942 – 2016) American Boxer and civil rights campaigner
Mahatma Gandhi (1869 – 1948) Leader of Indian independence movement
Margaret Thatcher (1925 – 2013) British Prime Minister 1979 – 1990
Mother Teresa (1910 – 1997) Macedonian Catholic missionary nun
Christopher Columbus (1451 – 1506) Italian explorer
Charles Darwin (1809 – 1882) British scientist, theory of evolution
Elvis Presley (1935 – 1977) American musician
Albert Einstein (1879 – 1955) German scientist, theory of relativity
Paul McCartney (1942 – ) British musician, member of Beatles
Queen Victoria (1819 – 1901) British monarch 1837 – 1901
Pope Francis (1936 – ) First pope from the Americas\
'''

top_20_list = [i for i in famous_list.split('\n')]
print(top_20_list)

#Part A
country = "Italian"
occupation1 = "Painter"
occupation2 = "Scientist"
for person in top_20_list:
    if country in person:
        if occupation1 in person:
            if occupation2 in person:
                print(person, '\nYes, you found an Italian person who is also a painter and scientist\n')
            else:print(f'\nNope, there is no {country}, {occupation1}, {occupation2} in the top 20 list.')


#Part B
def find_famous(famous_check, top_20_list):
    famous_count = 0
    for person in top_20_list:
        if famous_check in person:
            famous_count += 1
            if famous_count >= 1:
                print(f'\nYup, {famous_check} did make the Top 20 cut!')
            else:
                print(f'Sorry, {famous_check} did not make the Top 20 cut!')

famous_check = input('\nPlease Enter the name of the famous individual? ')
find_famous(famous_check, top_20_list)
