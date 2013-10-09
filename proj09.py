##Section 11
##Project 09
##11-19-12

def Parse_President(File):
    '''
    Description: Takes a file object and makes dicitonaries for the years the rpesident served, adn one for the party the president belonged to
    Requires: File Object
    Returns: Two dictionaries
    '''
    president = {}
    parties = {}
    for line in File:
        line = line.strip()
        Tmp_list = line.split(',')
        parties[Tmp_list[0]] = Tmp_list[1]
        Slice = Tmp_list[2:]
        for i in Slice:
            president[int(i)] = Tmp_list[0]
    return president,parties

def Parse_data(File):
    '''
    Description: Takes a file object adn makes a list of lists, containing all the data values as strings
    Requires:File object
    Returns:List of lists or raw data
    '''
    data = []
    line_num = 1
    for line in File:
        if line_num > 12:
            line = line.strip()
            Tmp_list = line.split(',')
            data.append(Tmp_list)
        line_num += 1
    return data

def Get_totals(Data,Presidents):
    '''
    Description: Takes a list of raw data, and a dictionary of years adn the associated president. It then creates an output list, with the total jobs and their associated president
    Requires: List Data, Dictionary Presidents
    Returns: List Output
    '''
    Output = []
    PreOutput = {}
    for i in Data:
        i[0] = int(i[0])
        try:
            PreOutput[Presidents[i[0]-1]].append(i[1])
            PreOutput[Presidents[i[0]]].extend(i[1:])
        except KeyError:
            PreOutput[Presidents[i[0]]] = []
            PreOutput[Presidents[i[0]]].extend(i[1:])
    for i in PreOutput:
        k = PreOutput[i]
        Tmp_list = [i]
        Before = int(k[0])
        total = 0
        for j in k:
            if j == '':
                continue
            j = int(j)
            total += j -Before
            Before = j
        Tmp_list.append(total)
        Output.append(Tmp_list)
    return Output

def Print_output(Output,Parties):
    '''
    Description: Takes the number of jobs each president has created or destroyed as a list of lists. It also takes a dictionary, Parties so the presidents may be seperated
    Requires: List Output, and Dictionary Parties
    Returns: None, but prints output to the console.
    '''
    Rep_total = 0
    Dem_total = 0
    print("Republicans:")
    for i in Output:
        if Parties[i[0]] == "Republican":
            Rep_total += i[1]
            if i[1] > 0:
                print(i[0], ":",abs(round(i[1]/1000,1)), "Million created jobs")
            else:
                print(i[0], ":",abs(round(i[1]/1000,1)), "Millon lost jobs")

    print("\nTotal jobs created:", abs(round(Rep_total/1000,1)), "Million jobs" )
    print("\n----------\n")
    print("Democrats:")
    for i in Output:
        if Parties[i[0]] == "Democrat":
            Dem_total += i[1]
            if i[1] > 0:
                print(i[0], ":",abs(round(i[1]/1000,1)), "Million created jobs")
            else:
                print(i[0], ":",abs(round(i[1]/1000,1)), "Million lost jobs")
    print("\nTotal jobs created:", abs(round(Dem_total/1000,1)), "Million jobs" )
    print("\n----------\n")
    print("The numbers overall are accurate but the individual numbers are off because of terms ending too soon.")
    print("This data show that while president clinton's numbers were off, his point still stands.")

def main():
    '''
    Description: ain fucniton that does everything
    Requires: None
    Returns: None
    '''
    President_file = open('Presidents.txt','r')
    Data_file = open('BLS_private.csv','r')
    Presidents,Parties = Parse_President(President_file)
    Data = Parse_data(Data_file)
    Output = Get_totals(Data,Presidents)
    Print_output(Output,Parties)
    President_file.close()
    Data_file.close()
    
if __name__ == "__main__":
    main()

