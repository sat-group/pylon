package cmu.edu;

import java.io.FileNotFoundException;
import java.io.IOException;

import org.sat4j.minisat.SolverFactory;
import org.sat4j.reader.DimacsReader;
import org.sat4j.reader.ParseFormatException;
import org.sat4j.reader.Reader;
import org.sat4j.specs.ContradictionException;
import org.sat4j.specs.IProblem;
import org.sat4j.specs.ISolver;
import org.sat4j.specs.TimeoutException;

public class UnitPropagation {
	
	public static void main(String[] args) {
		ISolver solver = SolverFactory.newDefault();
		solver.setTimeout(3600); // 1 hour timeout
		Reader reader = new DimacsReader(solver);
		if (args.length != 2) {
			System.out.println("Error: not enough parameters");
			System.out.println("Usage: java -jar up.jar <filename:string> <fixpoint:{0,1}>");
			System.exit(0);
		}
		
		try {
			IProblem problem = reader.parseInstance(args[0]);
			Integer fixpoint = Integer.valueOf(args[1]);
			problem.isSatisfiable(fixpoint == 1);
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
