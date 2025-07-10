class Main:
    def handle(self, input_str):
        """
        ***********************************************
        * This method parses each input and assigns it *
        * to different variables.                      *
        ***********************************************

        Format of input_str: "2, 7, 11, 15 | 9"
        - An array followed by a target integer, separated by '|'

        Your final output needs to be printed to the console.
        """

        parts = input_str.strip().split(" | ")
        nums_str, target_str = parts[0], parts[1]

        # Parse array and integer
        nums = [int(x.strip()) for x in nums_str.split(",")]
        target = int(target_str)

        # Output
        print("Array:", nums)
        print("Target:", target)
