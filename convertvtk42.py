from vtk import *
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='convert vtk file format to 4.2 version (works for MITK2018)')

    parser.add_argument('invtk', help='input vtk file')
    parser.add_argument('outvtk', help='output vtk file')
    args = parser.parse_args()    
        
    reader=vtkPolyDataReader();
    reader.SetFileName(args.invtk)
    reader.Update()
    geomFilter=vtkGeometryFilter()
    geomFilter.SetInputConnection(reader.GetOutputPort())
    geomFilter.Update()

    writer = vtkPolyDataWriter()
    #writer.SetFileTypeToBinary()
    writer.SetInputData(geomFilter.GetOutput())
    writer.SetFileName(args.outvtk)
    writer.SetFileVersion(42)
    writer.Write()
