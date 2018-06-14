package cmu.edu;

import java.io.FileNotFoundException;
import java.io.IOException;
import org.sat4j.core.VecInt;
import org.sat4j.pb.IPBSolver;
import org.sat4j.pb.SolverFactory;
import org.sat4j.reader.DimacsReader;
import org.sat4j.reader.ParseFormatException;
import org.sat4j.reader.Reader;
import org.sat4j.specs.ContradictionException;
import org.sat4j.specs.IProblem;
import org.sat4j.specs.TimeoutException;

public class Checker {

	public static void main(String[] args) {
		IPBSolver solver = SolverFactory.newDefault();
		solver.setTimeout(3600); // 1 hour timeout
		Reader reader = new DimacsReader(solver);
		try {
			IProblem problem = reader.parseInstance(args[0]);
			Integer n = Integer.parseInt(args[1]);
			VecInt constraint = new VecInt();
			for (int i = 1; i <= n; i++) {
				constraint.push(i);
			}

			if (solver.nVars() < n) {
				System.out.println("BUG! INCORRECT ENCODING!");
				System.out.println("Number of variables (" + solver.nVars() + ") is smaller than n (" + n + ")");
			
			} else {

				solver.addAtLeast(constraint, 2);
				if (problem.isSatisfiable()) {
					System.out.println("BUG! INCORRECT ENCODING!");
					System.out.println("Counterexample:");
					for (int i = 0; i < n; i++) {
						if (problem.model()[i] > 0)
							System.out.println("x" + (i + 1) + " = 1");
					}
				} else {
					System.out.println("CORRECT ENCODING!");
				}
			}
		} catch (FileNotFoundException e) {
			System.out.println("Exception" + e);
		} catch (ParseFormatException e) {
			System.out.println("Exception" + e);
		} catch (IOException e) {
			System.out.println("Exception" + e);
		} catch (ContradictionException e) {
			System.out.println("CORRECT ENCODING!");
		} catch (TimeoutException e) {
			System.out.println("Exception" + e);
		}
	}
}
