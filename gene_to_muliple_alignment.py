import requests
import argparse

def get_dna_sequence(accession_number):
    url = "https://www.ncbi.nlm.nih.gov/nuccore/{}/protein".format(accession_number)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["sequence"]
    else:
        return None

def get_multiple_alignment(accession_numbers):
    sequences = [get_dna_sequence(accession_number) for accession_number in accession_numbers]
    alignment = ""
    for sequence in sequences:
        alignment += sequence + "\n"
    return alignment

def main():
    parser = argparse.ArgumentParser(description="Get multiple sequence alignment from NCBI")
    parser.add_argument("--accessions", "-a", type=str, nargs="+", help="Comma-separated list of accession numbers")
    args = parser.parse_args()

    accession_numbers = args.accessions
    alignment = get_multiple_alignment(accession_numbers)
    print(alignment)

if __name__ == "__main__":
    main()
