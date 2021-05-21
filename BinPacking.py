from ortools.sat.python import cp_model
import Data
from Writer import Writer

class BinPacking:

    def __init__( self , _weights , _values , _bin_capacities ):
        self.parser = Data.DataBinPacking( _weights , _values , _bin_capacities )

    def parseSolution( self , data , solver , x):
        """Display the solution."""
        total_weight = 0
        total_value = 0
        res = { }
        bins = { }
        for b in data['all_bins']:
            curr = []
            bin_weight = 0
            bin_value = 0
            for idx, val in enumerate(data['weights']):
                if solver.Value(x[(idx, b)]) > 0:
                    curr.append( idx )
                    bin_weight += val
                    bin_value += data['values'][idx]
            total_weight += bin_weight
            total_value += bin_value
            bins[ b ] = curr

        res['bins'] = bins
        res['totalWeightPacked'] = total_weight
        res['totalValuePacked'] = total_value
        return res

    def multipleKnapsack(self , TIME_LIMIT = 1 ):
        data = self.parser.create_data_model()
        model = cp_model.CpModel()

        # Main variables.
        x = {}
        for idx in data['all_items']:
            for b in data['all_bins']:
                x[(idx, b)] = model.NewIntVar(0, 1, 'x_%i_%i' % (idx, b))
        max_value = sum(data['values'])
        # value[b] is the value of bin b when packed.
        value = [
            model.NewIntVar(0, max_value, 'value_%i' % b) for b in data['all_bins']
        ]
        for b in data['all_bins']:
            model.Add(value[b] == sum(
                x[(i, b)] * data['values'][i] for i in data['all_items']))

        # [START constraints]
        # Each item can be in at most one bin.
        for idx in data['all_items']:
            model.Add(sum(x[idx, b] for b in data['all_bins']) <= 1)

        # The amount packed in each bin cannot exceed its capacity.
        for b in data['all_bins']:
            model.Add(
                sum(x[(i, b)] * data['weights'][i]
                    for i in data['all_items']) <= data['bin_capacities'][b])
        # [END constraints]

        # Maximize total value of packed items.
        model.Maximize( sum(value) )

        solver = cp_model.CpSolver()

        status = solver.Solve(model)

        if status == cp_model.OPTIMAL:
            # Writer().print_solutions_bin_packing(data, solver, x)
            return self.parseSolution( data , solver , x )
        return dict()

def main():
    weights = [48, 30, 42, 36, 36, 48, 42, 42, 36, 24, 30, 30, 42, 36, 36]
    values = [10, 30, 25, 50, 35, 30, 15, 40, 30, 35, 45, 10, 20, 30, 25]
    bin_capacities = [100, 100, 100, 100, 100]
    solver = BinPacking( weights , values , bin_capacities )
    ans = solver.multipleKnapsack(  )
    print( ans )

if __name__ == '__main__':
    main()