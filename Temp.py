from vidstab import VidStab
import matplotlib.pyplot as plt
stabilizer = VidStab()
stabilizer.stabilize(input_path=r'Data\Test.mp4', output_path='results.avi', border_type='reflect')

stabilizer.plot_trajectory()
plt.show()

stabilizer.plot_transforms()
plt.show()
